import pandas as pd
from .llm import llm


def generate_campaign_report(df: pd.DataFrame, output_path: str):
    """
    Generates an AI-written markdown campaign report.
    """

    # ---- Basic stats (Python, deterministic) ----
    total_leads = len(df)
    emails_sent = df["personalized_email"].notna().sum()

    priority_counts = df["priority"].value_counts().to_dict()
    status_counts = df["status"].value_counts().to_dict()

    # ---- Prepare summary for LLM ----
    stats_summary = f"""
    Campaign Statistics:
    - Total leads: {total_leads}
    - Emails sent: {emails_sent}

    Priority breakdown:
    {priority_counts}

    Response breakdown:
    {status_counts}
    """

    # ---- LLM prompt ----
    prompt = f"""
    You are a sales analytics assistant.

    Using the campaign statistics below, write a concise markdown report.

    RULES:
    - Use clear headings
    - Highlight performance trends
    - Mention what worked well
    - Mention improvement opportunities
    - Keep it short (8–12 lines)
    - Do NOT invent numbers

    Statistics:
    {stats_summary}

    Output:
    """

    response = llm.invoke(prompt)
    report_text = response.content.strip()

    # ---- Save markdown report ----
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    return output_path
