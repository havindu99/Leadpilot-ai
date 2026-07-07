# 🚀 LeadPilot AI

**AI-Powered Lead & Message Triage Platform**

Smarter Lead Management. Faster Decisions.

LeadPilot AI is a Streamlit-based dashboard that automatically analyzes incoming
customer messages, classifies them by category and priority, scores leads, and
surfaces the ones that need human attention — so your sales team can focus on
what matters.

---

## ✨ Features

- **📊 Real-time Dashboard** — Live overview of total messages, high-priority
  items, qualified leads, and filtered spam.
- **🤖 AI Message Analysis** — Automatic categorization (e.g. Sales Inquiry,
  Complaint, Mobile App Development) and sentiment detection (Positive /
  Neutral / Negative).
- **🔥 Priority Scoring** — Messages are ranked High / Medium / Low so urgent
  leads never get buried.
- **⭐ Lead Scoring** — Each lead gets a numeric score to help reps prioritize
  follow-ups.
- **📈 Analytics & Reports** — Category distribution, priority breakdown, and
  historical trends.
- **📜 Recent Activity Feed** — A live, filterable log of the latest triaged
  messages.
- **🕘 History** — Full searchable record of past messages and decisions.
- **⚙️ Configurable Settings** — Tune thresholds, categories, and integrations
  from the Settings page.

---

## 🗂️ Project Structure

```
LeadPilot-AI/
├── app.py                     # Application entry point
├── app/                        # Streamlit multipage app screens
│   ├── Analytics.py
│   ├── Dashboard.py
│   ├── History.py
│   ├── Message_Analyzer.py
│   ├── Reports.py
│   └── Settings.py
├── assets/                    # Static assets (images, icons)
├── components/                # Reusable UI building blocks
│   ├── charts.py               # Plotly chart builders
│   ├── footer.py                # App footer
│   ├── header.py                # App header / hero section
│   ├── metric_cards.py          # KPI / stat cards
│   └── sidebar.py                # Sidebar navigation
├── config/                     # App configuration
│   ├── settings.py              # General settings
│   └── theme.py                  # Theme constants
├── data/                        # Local/sample data
├── database/
│   └── leads.db                  # SQLite database of leads & messages
├── models/                       # Data models / schemas
├── reports/                      # Generated report output
├── services/                     # Business logic layer
│   ├── ai_service.py               # AI/LLM message analysis
│   ├── analytics_service.py        # Aggregations for charts & stats
│   ├── database_service.py         # Data access layer
│   ├── lead_scoring.py             # Lead scoring logic
│   └── report_service.py           # Report generation
├── styles/
│   └── style.css                    # Custom CSS theme
├── utils/                           # Shared helpers
├── venv/                            # Virtual environment (not committed)
├── .env                              # Environment variables (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

- **[Streamlit](https://streamlit.io/)** — UI framework
- **[Plotly](https://plotly.com/python/)** — Interactive charts
- **[Pandas](https://pandas.pydata.org/)** — Data wrangling
- **SQLite** — Lightweight local database
- **Python 3.10+**

---

## ⚡ Getting Started

### Prerequisites

- Python 3.10 or higher
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/havindu99/Leadpilot-ai.git
cd LeadPilot-AI

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root with the values your setup needs, for
example:

```
DATABASE_PATH=database/leads.db
AI_API_KEY=your_api_key_here
```

### Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## 📖 Usage

1. Go to **Message Analyzer** and paste or submit a customer message.
2. LeadPilot AI classifies it (category, priority, sentiment) and assigns a
   lead score.
3. View the results instantly on the **Dashboard**.
4. Check **History** for a full audit trail, or **Reports** / **Analytics**
   for summarized insights and trends.
5. Adjust thresholds and preferences under **Settings**.

---

## 🤝 Contributing

Contributions are welcome! Please open an issue to discuss what you'd like to
change before submitting a pull request.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m "Add amazing feature"`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the `LICENSE` file for
details.

---

## 📬 Contact

Maintained by **havindu99**. For questions or support, please open an issue
on the [GitHub repository](https://github.com/havindu99/Leadpilot-ai).
