# 🤖 AI Corporate Analyst (Text-to-SQL Dashboard)

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-API-412991.svg)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)

An intelligent B2B web dashboard that allows users to query a relational database using natural language. No SQL knowledge required. The system translates plain English into database queries, executes them, and returns a human-readable analytical answer.

🔗 **[Live Demo](https://asimerole-text2sql.streamlit.app/)** 🔐 **Demo Password:** `demo123` *(Limited to 10 requests per session to prevent API abuse)*

---

## 🎯 How It Works (The Two-Loop AI Architecture)

This project implements a reliable AI agent workflow:
1. **User Input:** The user asks a business question (e.g., *"Who from Berlin spent more than 1000?"*).
2. **AI Loop 1 (Text-to-SQL):** The OpenAI API (`gpt-4o-mini`) acts as a strict SQL developer, translating the prompt into a valid SQLite query based on the injected database schema.
3. **Secure Execution:** The Python backend executes the generated SQL query locally against the database.
4. **AI Loop 2 (Data-to-Text):** The raw database output (e.g., `[('Anna',)]`) is sent back to the AI to generate a polite, human-readable summary.

## ✨ Key Features

* **Interactive UI:** Built entirely in Python using Streamlit. Includes a sidebar for real-time database preview.
* **Security & Rate Limiting:** Built-in authentication system. Implements `st.session_state` to track and limit API requests for demo users, protecting the OpenAI billing account.
* **Graceful Error Handling:** Catches and displays database or syntax errors without crashing the application.
* **Environment Protection:** API keys and admin passwords are securely managed via `.env` and Streamlit Secrets.

## 🛠️ Tech Stack

* **Language:** Python
* **Frontend/Framework:** Streamlit
* **AI Provider:** OpenAI API (`gpt-4o-mini` model with `temperature=0` for strict SQL generation)
* **Database:** SQLite3

---

## 🚀 Local Installation & Setup

If you want to run this project locally, follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/asimerole/Text-to-SQL-Dashboard.git](https://github.com/asimerole/Text-to-SQL-Dashboard.git)
cd Text-to-SQL-Dashboard
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```
**3. Set up environment variables**
Create a `.env` file in the root directory and add your credentials:
```bash
OPENAI_API_KEY=sk-your-openai-api-key
ADM_PWD=your_admin_password
```

**4. Run the application**
```bash
streamlit run web.py
```

The app will automatically create a local `sales.db` with sample data on the first run.

Created as a portfolio project showcasing AI integration into business workflows.