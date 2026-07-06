import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def test_ai():
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Say hello in one sentence."
    )
    return response.text


def analyze_message(message):

    prompt = f"""
    You are an AI Lead Triage Assistant.

    Analyze the customer message and return ONLY valid JSON.

    Do NOT return markdown.
    Do NOT use ```json.
    Return only JSON.

    Customer Message:
    {message}

    JSON format:
    {{
        "category": "",
        "priority": "",
        "lead_score": 0,
        "sentiment": "",
        "urgency": "",
        "suggested_reply": "",
        "next_action": "",
        "human_review": "",
        "confidence": 0,
        "reason": ""
    }}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()
    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    return json.loads(text)