#!/bin/bash

PROJECT_DIR="/root/davidPhan_alphashere_test_assignment"

cd "$PROJECT_DIR"

# Ghi log ra file
echo "[🕒] $(date) - Bắt đầu chạy pipeline" >> logs/cron.log

# Chạy docker container
docker run --rm --env-file .env -v "$PROJECT_DIR/data:/app/data" optibot >> logs/cron.log 2>&1

echo "[✅] $(date) - Hoàn tất pipeline" >> logs/cron.log
