import pandas as pd
import time

from .persona import persona_agent
from .priority import calculate_priority
from .email_writer import email_writer_agent
from .email_sender import send_email
from .response_simulator import simulate_response
from .report import generate_campaign_report   


def run_pipeline(input_csv_path: str, output_csv_path: str):
    df = pd.read_csv(input_csv_path)

    # ---------- Persona enrichment ----------
    rows_need_persona = df[df["persona"].isna()]

    for idx, row in rows_need_persona.iterrows():
        state = {
            "lead": row.to_dict(),
            "persona": None,
            "priority": None
        }
        state = persona_agent(state)
        df.loc[idx, "persona"] = state["persona"]

    # ---------- Priority scoring ----------
    if "priority_score" not in df.columns:
        df["priority_score"] = None

    df[["priority_score", "priority"]] = df.apply(
        lambda row: calculate_priority(row),
        axis=1,
        result_type="expand"
    )

    # ---------- Email generation + sending ----------
    if "personalized_email" not in df.columns:
        df["personalized_email"] = None

    if "status" not in df.columns:
        df["status"] = None

    for idx, row in df.iterrows():

        # skip if no email
        if pd.isna(row.get("email")):
            continue

        priority = str(row["priority"]).strip().lower()

        # only high & medium get emails
        if priority not in ["high", "medium"]:
            df.at[idx, "status"] = simulate_response(row["priority"])
            continue

        state = {"lead": row.to_dict()}
        email_text = email_writer_agent(state)

        # save email text
        df.at[idx, "personalized_email"] = email_text

        # send email
        send_email(
            to_email=row["email"],
            subject="Quick question about your current workflow",
            body=email_text
        )

        # simulate response
        df.at[idx, "status"] = simulate_response(row["priority"])

        time.sleep(1)  

    # ---------- Save final CSV ----------
    df.to_csv(output_csv_path, index=False)

    # ---------- Generate campaign report (LLM) ----------
    generate_campaign_report(
        df=df,
        output_path="reports/campaign_summary.md"
    )

    return output_csv_path
