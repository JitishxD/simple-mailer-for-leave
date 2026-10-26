"""Builds and sends the email using Gmail's SMTP server."""

import smtplib
import ssl
from email.message import EmailMessage
from email.utils import formataddr

from config import SMTP_HOST, SMTP_PORT


def split_addresses(text: str) -> list[str]:
    return [a.strip() for a in text.split(",") if a.strip()]


def build_message(sender, sender_name, to, cc, subject, body) -> EmailMessage:
    msg = EmailMessage()
    msg["From"] = formataddr((sender_name, sender))
    msg["To"] = ", ".join(split_addresses(to))
    if split_addresses(cc):
        msg["Cc"] = ", ".join(split_addresses(cc))
    msg["Subject"] = subject
    msg.set_content(body)  # UTF-8 plain text
    return msg


def send(msg: EmailMessage, sender: str, password: str) -> None:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as server:
        server.login(sender, password)
        server.send_message(msg)  # sends to both To and Cc
