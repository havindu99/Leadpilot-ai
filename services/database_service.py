import sqlite3
from pathlib import Path
from datetime import datetime
import pandas as pd

DB_PATH = Path("database/leads.db")


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            message TEXT,
            category TEXT,
            priority TEXT,
            lead_score INTEGER,
            sentiment TEXT,
            urgency TEXT,
            suggested_reply TEXT,
            next_action TEXT,
            human_review TEXT,
            confidence INTEGER,
            reason TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_lead(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO leads (
            source, message, category, priority, lead_score,
            sentiment, urgency, suggested_reply,
            next_action, human_review, confidence,
            reason, created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("source"),
        data.get("message"),
        data.get("category"),
        data.get("priority"),
        int(data.get("lead_score", 0)),
        data.get("sentiment"),
        data.get("urgency"),
        data.get("suggested_reply"),
        data.get("next_action"),
        data.get("human_review"),
        int(data.get("confidence", 0)),
        data.get("reason"),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_recent_leads(limit=10):
    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT source, category, priority, lead_score, sentiment, created_at
        FROM leads
        ORDER BY id DESC
        LIMIT ?
        """,
        conn,
        params=(limit,)
    )

    conn.close()
    return df


def get_dashboard_stats():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM leads")
    total_messages = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM leads WHERE priority = 'High'")
    high_priority = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM leads WHERE lead_score >= 70")
    qualified_leads = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM leads WHERE category = 'Spam'")
    spam_messages = cursor.fetchone()[0]

    conn.close()

    return {
        "total_messages": total_messages,
        "high_priority": high_priority,
        "qualified_leads": qualified_leads,
        "spam_messages": spam_messages
    }


def get_category_distribution():
    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT category AS Category, COUNT(*) AS Count
        FROM leads
        GROUP BY category
        """,
        conn
    )

    conn.close()
    return df


def get_priority_distribution():
    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT priority AS Priority, COUNT(*) AS Count
        FROM leads
        GROUP BY priority
        """,
        conn
    )

    conn.close()
    return df