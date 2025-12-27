import smtplib
from email.message import EmailMessage


SMTP_HOST = "mailhog"   # Docker service name
SMTP_PORT = 1025        # MailHog SMTP port
FROM_EMAIL = "sales@demo-crm.ai"


def send_email(to_email: str, subject: str, body: str):
    msg = EmailMessage()
    msg["From"] = FROM_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.send_message(msg)
