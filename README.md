# 🔥 Viral Content Machine — Facebook Auto Poster v2

A **psychology-driven Facebook content engine** that generates viral posts with Groq-hosted Llama models, creates AI image creatives through Pollinations.ai, and can publish approved posts to a Facebook Page.

---

## ✨ Features

| Feature | Status |
|---|---|
| 12 psychology-backed hook styles | ✅ |
| 3 post variations (Emotional / Educational / Bold) | ✅ |
| 4-part structured post format (Hook → Value → Punch → CTA) | ✅ |
| Anti-generic filter for clichéd output | ✅ |
| Niche optimization (AI/Tech, Motivation, ASMR, Business) | ✅ |
| Tone control slider (Safe → Balanced → Aggressive) | ✅ |
| Roman Urdu and Hinglish generation modes | ✅ |
| AI image prompt + Pollinations image render | ✅ |
| Local history and analytics tab | ✅ |
| Streamlit UI + optional GitHub Actions auto-posting | ✅ |

---

## 🚀 Deploy to Streamlit Cloud

### Step 1 — Fork this repo
Click **Fork** on GitHub to copy it to your account.

### Step 2 — Get a Groq API key
Go to [console.groq.com](https://console.groq.com) → **API Keys** → create an API key.

### Step 3 — Deploy
1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
2. Click **New app** → select your forked repo.
3. Set **Main file path** to `app.py`.
4. Click **Advanced settings → Secrets** and paste:
   ```toml
   GROQ_API_KEY = "gsk_your_key_here"
   ```
5. Click **Deploy**.

> Existing deployments that still use `GEMINI_API_KEY` continue to work as a legacy fallback, but new installs should use `GROQ_API_KEY`.

---

## 💻 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the **Settings** tab and save:

- Groq API key
- Facebook Page Access Token
- Facebook Page ID

Local credentials are saved to `fb_config.json`, which should stay uncommitted.

---

## 🤖 GitHub Actions Auto Posting

The workflow in `.github/workflows/auto_post.yml` can run scheduled posts without Streamlit. Add these repository secrets:

| Secret | Purpose |
|---|---|
| `GROQ_API_KEY` | Groq chat-completions key |
| `FB_PAGE_TOKEN` | Facebook Page access token |
| `FB_PAGE_ID` | Facebook Page ID |

---

## 🗂️ Files

| File | Purpose |
|---|---|
| `app.py` | Main Streamlit UI, scheduler, settings, manual posting |
| `engine.py` | Groq generation, hook library, quality filters, image generation/upload helpers |
| `analytics.py` | Local history tracking and aggregate stats |
| `auto_post.py` | Standalone GitHub Actions posting script |
| `.github/workflows/auto_post.yml` | Scheduled/manual GitHub Actions workflow |
| `requirements.txt` | Streamlit app dependencies |
| `fb_config.json` | Auto-created local credentials — **gitignored, never commit** |
| `fb_history.json` | Auto-created local post history — **gitignored, never commit** |
| `schedule_log.json` | Auto-created scheduler log — **gitignored, never commit** |

---

## 🧠 Hook Styles

Curiosity Gap · Controversy · Fear/Loss · Authority+Data · Relatable Pain · Bold Claim · Story Hook · List Promise · Provocative Question · Shocking Statistic · Direct Call-Out · Transformation Promise

---

## ⚡ Manual Workflow

1. Sidebar → select niche, hook style, tone, language, and image preference.
2. Click **⚡ Generate 3 Variations**.
3. Review Emotional / Educational / Bold tabs.
4. Edit the selected draft.
5. Click **🚀 Approve & Post** and approve image or text-only publishing.
6. Review **📜 History** and **📊 Analytics**.
