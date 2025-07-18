# Các thư viện cần thiết
import os
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import openai
import requests                     # Gửi HTTP request để gọi API Zendesk
from bs4 import BeautifulSoup       # Dùng để xử lý HTML
from markdownify import markdownify as md  # Chuyển HTML sang Markdown
from dotenv import load_dotenv      # Đọc biến môi trường từ file .env
from utils.ai_html_filter import clean_html

# Tải các biến môi trường từ file .env vào biến môi trường hệ thống
load_dotenv()

# Lấy thông tin cấu hình từ biến môi trường
ZENDESK_DOMAIN = os.getenv("ZENDESK_DOMAIN")
ZENDESK_EMAIL = os.getenv("ZENDESK_EMAIL")
ZENDESK_API_TOKEN = os.getenv("ZENDESK_API_TOKEN")

# URL gốc của Zendesk Help Center API (dành cho bài viết tiếng Anh)
BASE_URL = f"https://{ZENDESK_DOMAIN}/api/v2/help_center/en-us/articles.json"

# Header chuẩn cho request (có thể mở rộng thêm nếu cần)
HEADERS = {
    "Content-Type": "application/json"
}

# Hàm lấy danh sách tất cả các bài viết từ Zendesk
def fetch_articles():
    articles = []
    url = BASE_URL  # Trang đầu tiên

    while url:  # Zendesk phân trang → lặp qua từng trang kết quả
        res = requests.get(
            url,
            auth=(f"{ZENDESK_EMAIL}/token", ZENDESK_API_TOKEN),  # Basic Auth với token
            headers=HEADERS
        )
        data = res.json()
        articles.extend(data["articles"])        # Thêm bài viết vào danh sách
        url = data.get("next_page")              # Nếu có trang tiếp theo thì tiếp tục lặp

    return articles  # Trả về danh sách tất cả bài viết

# Hàm lưu một bài viết thành file Markdown
def save_markdown(article):
    title = article["title"]                     # Lấy tiêu đề bài viết
    body_html = article["body"]                  # Nội dung dạng HTML
    slug = article["html_url"].split("/")[-1]    # Dùng phần cuối URL làm tên file

    # lọc và xoá quảng cáo/navigation trong HTML
    soup = BeautifulSoup(body_html, "html.parser")  # Phân tích HTML bằng BeautifulSoup
    soup = clean_html(soup)  # dùng hàm wrapper tự động lọc (AI hoặc basic)

    markdown = md(str(soup), heading_style="ATX")  # Chuyển HTML → Markdown

    filename = f"data/{slug}.md"                    # Đường dẫn file Markdown

    # Ghi nội dung Markdown ra file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")  # Thêm tiêu đề Markdown
        f.write(markdown)          # Thêm nội dung

# Hàm chính gọi toàn bộ quy trình scraper
def run_scraper():
    print("[*] Fetching articles...")
    articles = fetch_articles()                   # Gọi hàm fetch
    print(f"[+] Found {len(articles)} articles.") # Thông báo số lượng

    if not openai.api_key and not os.getenv("OPENAI_API_KEY"):
            print("[⚠️] Không tìm thấy OpenAI API key. Đang sử dụng clean_html_basic thay thế.")
    for article in articles:                      # Với mỗi bài viết
        save_markdown(article)                    # Lưu ra file Markdown

    print("[✓] Articles saved to ./data/")

# Nếu chạy trực tiếp file này thì gọi run_scraper()
if __name__ == "__main__":
    run_scraper()
