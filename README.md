# AI-Enhanced Sales Campaign CRM (MVP)

This project is a lightweight, end-to-end **AI-powered Sales Campaign CRM** .

The system ingests leads from a CSV file, enriches them using an LLM, prioritizes leads, generates personalized outreach emails, simulates responses, and produces a campaign summary — all runnable via **Docker Compose**.

---

##  Features

- **Lead Ingestion**
  - Upload leads via CSV file from a simple web UI
- **AI Enrichment**
  - Infer missing buyer persona using a free LLM (Groq)
- **Lead Scoring & Prioritization**
  - Deterministic Python-based scoring (High / Medium / Low)
- **Personalized Outreach Emails**
  - LLM-generated short, professional cold emails
- **Email Sending (Local Testing)**
  - Emails sent to **MailHog** (no real emails sent)
- **Response Simulation**
  - Fake responses generated to simulate campaign outcomes
- **Campaign Report**
  - Auto-generated markdown summary with campaign insights
- **Dockerized**
  - Run everything with a single command -> docker compose up but initially needed docker compose --build

---

## Tech Stack

- **FastAPI** – Backend & upload UI
- **LangChain + Groq LLM** – Persona & email generation
- **Pandas** – CSV processing
- **Docker & Docker Compose** – Orchestration
- **MailHog** – Local email testing
- **Python 3.11+**

---

## 📂 Project Structure
   ai-sales-crm-mvp/
│
├── app/
│ ├── main.py # FastAPI entry point
│ ├── pipeline.py # End-to-end campaign pipeline
│ ├── persona.py # Persona enrichment agent
│ ├── priority.py # Lead scoring logic
│ ├── email_writer.py # Personalized email generator
│ ├── email_sender.py # SMTP / MailHog sender
│ ├── response_simulator.py # Fake response generator
│ └── llm.py # Groq LLM configuration
│
├── templates/
│ └── index.html # CSV upload UI
│
├── data/
│ ├── input/ # Uploaded CSV files (runtime)
│ └── output/ # Processed CSV files (runtime)
│
├── reports/
│ └── campaign_summary.md # Auto-generated report
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md

