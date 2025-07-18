import openai
import os
from bs4 import BeautifulSoup, Tag
from typing import List, Dict

# NOTE: set your OpenAI key in your env before calling this function
# or set openai.api_key manually before import

def classify_blocks_via_openai(blocks: List[Tag], max_blocks: int = 30) -> List[str]:
    """
    Phân loại các khối HTML sử dụng OpenAI.
    Trả về danh sách ID của các khối (BLOCK_0, BLOCK_1, ...) cần xoá.
    """
    selected_blocks = blocks[:max_blocks]
    id_to_tag: Dict[str, Tag] = {}
    prompt_lines = []

    # Duyệt qua từng block nghi ngờ và gán ID dạng BLOCK_0, BLOCK_1...
    for i, tag in enumerate(selected_blocks):
        block_id = f"BLOCK_{i}"
        id_to_tag[block_id] = tag
        content = tag.get_text(separator=' ', strip=True)
        if not content or len(content) < 30:
            continue  # Bỏ qua khối trống hoặc quá ngắn
        prompt_lines.append(f"{block_id}:{content[:500]}")

    if not prompt_lines:
        return []

    # Prompt yêu cầu OpenAI đánh dấu các block nên xoá
    prompt = (
        "Below are several content blocks extracted from a Zendesk help article.\n"
        "Please identify which of these blocks are non-essential, such as advertisements, navigation menus, related links, or any content not part of the main instructional or informative body.\n"
        "\nReply with a comma-separated list of the BLOCK IDs that should be removed.\n"
        "For example: BLOCK_0, BLOCK_2, BLOCK_5\n"
        "\nOnly include the IDs in your answer.\n\n"
        + "\n\n".join(prompt_lines)
    )

    print("[🤖] Đang gửi yêu cầu phân loại các khối HTML đến OpenAI...")

    # Gọi OpenAI ChatCompletion API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    # Phân tích kết quả: trích ra danh sách BLOCK_? từ câu trả lời
    content = response["choices"][0]["message"]["content"]
    selected_ids = [line.strip().upper() for line in content.replace(",", "\n").splitlines() if line.strip().startswith("BLOCK_")]

    return selected_ids

def clean_html_basic(soup: BeautifulSoup) -> BeautifulSoup:
    """
    Dọn dẹp HTML cơ bản không cần dùng OpenAI.
    Xoá các khối có class/id liên quan đến quảng cáo, điều hướng, sidebar, v.v.
    """
    suspect_keywords = ["ads", "advertisement", "sidebar", "footer", "nav", "breadcrumb", "related", "promo"]
    for tag in soup.find_all(True):
        tag_class = " ".join(tag.get("class", [])).lower()
        tag_id = (tag.get("id") or "").lower()
        if any(kw in tag_class or kw in tag_id for kw in suspect_keywords):
            print(f"[🧹] Đã xoá <{tag.name} class='{tag_class}' id='{tag_id}'> (basic filter)")
            tag.decompose()
    return soup

def clean_html(soup: BeautifulSoup, max_blocks: int = 30) -> BeautifulSoup:
    """
    Hàm wrapper: tự động tìm, phân loại và xoá các block không cần thiết khỏi soup.
    Nếu không có OpenAI API key thì fallback sang clean_html_basic().
    """
    if not openai.api_key and not os.getenv("OPENAI_API_KEY"):
        return clean_html_basic(soup)

    suspects = soup.find_all(["div", "aside", "nav", "footer"])
    to_remove = classify_blocks_via_openai(suspects, max_blocks=max_blocks)

    for i, tag in enumerate(suspects[:max_blocks]):
        block_id = f"BLOCK_{i}"
        if block_id in to_remove:
            print(f"[🧹] Đã xoá {block_id} - <{tag.name} class={tag.get('class')}>")
            tag.decompose()

    return soup
