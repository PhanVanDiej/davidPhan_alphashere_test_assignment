# Base image Python 
FROM python:3.10-slim

# Tạo thư mục làm việc
WORKDIR /app

# Copy toàn bộ source code vào container
COPY . .

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Lệnh mặc định khi chạy container
CMD ["python", "main.py"]


