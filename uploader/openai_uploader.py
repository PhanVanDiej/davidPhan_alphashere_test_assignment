import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
DATA_DIR = "data/"

def upload_files_to_vector_store():
    print("[📁] Đang tải lên các file Markdown vào Vector Store...")

    # Bước 1: Tạo Vector Store
    vector_store = openai.beta.vector_stores.create(name="optibot-support-articles")
    vector_store_id = vector_store.id
    print(f"[✅] Đã tạo Vector Store ID: {vector_store_id}")

    # Bước 2: Duyệt qua tất cả file .md trong thư mục data/
    file_ids = []
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".md"):
            filepath = os.path.join(DATA_DIR, filename)
            with open(filepath, "rb") as f:
                print(f"[*] Đang upload: {filename}")
                uploaded_file = openai.files.create(file=f, purpose="assistants")
                file_ids.append(uploaded_file.id)

    # Bước 3: Gắn file vào Vector Store
    openai.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store_id,
        files=file_ids
    )
    print(f"[🎉] Đã upload {len(file_ids)} files vào Vector Store.")
    return vector_store_id

def create_assistant(vector_store_id):
    assistant = openai.beta.assistants.create(
        name="Optibot Assistant",
        instructions=(
            "You are OptiBot, the customer-support bot for OptiSigns.com.\n"
            "- Only answer based on uploaded docs.\n"
            "- Tone: helpful, factual, concise.\n"
            "- Use max 5 bullet points, else provide URL.\n"
            "- Cite up to 3 article URLs per reply."
        ),
        tools=[{"type": "retrieval"}],
        model="gpt-4",
        tool_resources={
            "file_search": {
                "vector_store_ids": [vector_store_id]
            }
        }
    )
    print(f"[🤖] Assistant đã được tạo với ID: {assistant.id}")
    return assistant.id

def run_upload():
    openai.api_key = os.getenv("OPTIBOT_ASSISTANT_KEY")

    if not openai.api_key or openai.api_key.strip() == "":
        print("[❌] Không tìm thấy OpenAI API key. Hãy thiết lập biến môi trường OPTIBOT_ASSISTANT_KEY.")
        return


    vs_id = upload_files_to_vector_store()
    assistant_id = create_assistant(vs_id)
    print("[🏁] Hoàn tất upload.")
    print(f"→ Vector Store ID: {vs_id}")
    print(f"→ Assistant ID: {assistant_id}")

if __name__ == "__main__":
    run_upload()
