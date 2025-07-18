from scraper.zendesk_scraper import run_scraper
from uploader.openai_uploader import run_upload

if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════╗
║      🚀 OPTIBOT MINI - AUTO PIPELINE       ║
╚════════════════════════════════════════════╝
""")
    print("""
Pipeline này sẽ thực hiện:
1️⃣  Tự động scrape bài viết từ Zendesk
2️⃣  Làm sạch nội dung (HTML ➜ Markdown)
3️⃣  Upload các file Markdown vào Vector Store
4️⃣  Tạo Assistant và liên kết dữ liệu

📌 Ghi chú:
- Do không có OpenAI API key → phần upload sẽ bị bỏ qua.
- Kết quả Markdown sẽ được lưu tại thư mục ./data
- Toàn bộ logic đã hoàn thành, chỉ cần thêm key cho biến
OPTIBOT_ASSISTANT_KEY trong file .env.
""")

    # Bước 1: scrape các bài viết từ Zendesk
    run_scraper()

    # Bước 2: upload Markdown lên OpenAI, tạo Assistant
    run_upload()

    print("\n[✅] Đã hoàn tất toàn bộ pipeline.")
