"""Leave mail generator — run: python main.py"""
import smtplib
import sys

from config import FIELDS
from auth import get_credentials
from mailer import build_message, send
from prompts import collect_details, confirm
from storage import load_defaults, save_last_used
from template import build_body, build_subject


def preview(msg) -> None:
    line = "=" * 60
    print(f"\n{line}\nPREVIEW\n{line}")
    print(f"From    : {msg['From']}")
    print(f"To      : {msg['To']}")
    print(f"Cc      : {msg['Cc'] or '-'}")
    print(f"Subject : {msg['Subject']}")
    print(line)
    print(msg.get_content())
    print(line)


def main() -> None:
    data = collect_details(FIELDS, load_defaults())

    if not data["to"].strip():
        sys.exit("Error: 'To' cannot be empty.")

    sender, password = get_credentials()
    msg = build_message(
        sender=sender,
        sender_name=data["name"],
        to=data["to"],
        cc=data["cc"],
        subject=build_subject(data),
        body=build_body(data),
    )

    preview(msg)
    save_last_used(data)

    if not confirm("Send this mail?"):
        print("Not sent. Your values were saved for next time.")
        return

    try:
        send(msg, sender, password)
        print("Mail sent successfully.")
    except smtplib.SMTPAuthenticationError:
        print("Login failed. Check GMAIL_ADDRESS and GMAIL_APP_PASSWORD in .env "
              "(use an App Password, not your normal password).")
    except Exception as e:
        print(f"Failed to send: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCancelled.")
    finally:
        input("\nPress Enter to close...")
