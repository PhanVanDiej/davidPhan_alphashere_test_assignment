# OptiBot Mini - Assignment (Alphashere)

This is a mini clone of OptiSigns' OptiBot, implemented for the Full Stack Developer Intern test assignment.

---

# 🧠 Overview

This bot automatically:

1. Scrapes help articles from Zendesk (OptiSigns support site)
2. Cleans HTML (removes ads/navigation, preserves code/links/headings)
3. Detects newly added or updated articles via hashing
4. Converts them to Markdown and saves to `data/`
5. Uploads them to OpenAI vector store and attaches them to an Assistant
6. Schedules the above pipeline to run daily on a DigitalOcean droplet

---

# 📁 Folder Structure

<img width="300" height="463" alt="image" src="https://github.com/user-attachments/assets/9969e413-31f4-469c-8516-47b2185bca68" />


---

# 🛠 Setup & Run
## 1. Clone & install
```
git clone https://github.com/<your-name>/<your-repo> 
cd your-repo \n
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


## 2. Configure `.env`
Create a file named `.env` with the same level `main.py`, like so:
```
ZENDESK_DOMAIN=yourdomain.zendesk.com
ZENDESK_EMAIL=your_email
ZENDESK_API_TOKEN=your_token
OPTIBOT_ASSISTANT_KEY=your_openai_key
```
You can copy properties in `.env.sample` and paste into `.env`.

# 🐳 Run with Docker
```
docker build -t optibot .
docker run --rm --env-file .env optibot
```

# 📅 Run Daily via Cron
This command runs daily via `crontab` on a DigitalOcean droplet, cus you cannot access the **Ubuntu server (Droplet)**, 
I just write the command here:
```bash
@daily bash run_pipeline.sh
```
It will be scheduled to run at 7:00 am every morning
Logs and artefacts are saved and included in repo for review:
- `logs/cron-YYYY-MM-DD.log`
- `artefacts/diff_summary.json`
---
# 🔍 Chunking Strategy
Each article → 1 Markdown file → 1 OpenAI file

No sub-chunking (articles are short)

Cleaned via BeautifulSoup + optional AI filter

Preserves: code blocks, relative links, headings

Filters: ads, nav, irrelevant blocks

AI-assisted filter (optional) can evaluate blocks before removal

