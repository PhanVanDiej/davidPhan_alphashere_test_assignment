import hashlib
import os
import json
from bs4 import BeautifulSoup

# Đảm bảo thư mục artefacts tồn tại
os.makedirs("artefacts", exist_ok=True)
HASH_FILE = os.path.join("artefacts", "article_hash.json")

def clean_html_for_hash(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup.find_all(["script", "style", "time"]):
        tag.decompose()

    for tag in soup.find_all(string=lambda s: s and any(word in s.lower() for word in ["last updated", "modified", "recent change"])):
        tag.extract()

    return soup.get_text(separator=" ", strip=True)

def calculate_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def load_previous_hashes() -> dict:
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r", encoding="utf-8") as f:
            raw = json.load(f)
            if isinstance(raw, dict):
                return {str(k): v for k, v in raw.items()}
            else:
                print("[❌] article_hash.json không đúng định dạng dict. Đã bỏ qua.")
                return {}
    return {}

def save_article_hashes(hash_map: dict):
    with open(HASH_FILE, "w", encoding="utf-8") as f:
        json.dump(hash_map, f, indent=2)

def detect_article_changes(articles: list) -> tuple:
    previous = load_previous_hashes()
    print(f"[📂] Đã load {len(previous)} hash từ file cũ.")

    current = {}
    added, updated, skipped = [], [], []

    for article in articles:
        slug = str(article["id"])
        title = article["title"]
        body = article["body"]
        cleaned_body = clean_html_for_hash(body)
        full = title.strip() + "\n" + cleaned_body
        h = calculate_hash(full)
        current[slug] = h

        if slug not in previous:
            added.append(article)
        elif previous[slug] != h:
            updated.append(article)
        else:
            skipped.append(article)

    save_article_hashes(current)
    print(f"[💾] Đã ghi {len(current)} hash vào {HASH_FILE}")
    return added, updated, skipped
