"""Loads your Gmail address and app password from .env (or asks for them)."""

import os
from getpass import getpass

from config import ENV_FILE


def _load_env_file(path: str) -> None:
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def get_credentials() -> tuple[str, str]:
    _load_env_file(ENV_FILE)

    # EXE BUILD: uncomment the two lines below, fill in your values,
    # then build your exe with: pyinstaller --icon=icon.ico --onefile main.py
    # address = "your_email@gmail.com"
    # password = "abcd efgh ijkl mnop"

    # Obv comment these two line when you're building the exe file
    address = os.environ.get("GMAIL_ADDRESS") or input("Your Gmail address: ").strip()
    password = os.environ.get("GMAIL_APP_PASSWORD") or getpass("Gmail App Password: ")

    return address, password.replace(" ", "")  # Google shows it with spaces
