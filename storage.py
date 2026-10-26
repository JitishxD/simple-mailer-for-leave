"""Remembers the last values you used, so next time Enter gives you those."""
import json
import os

from config import DEFAULTS, LAST_USED_FILE


def load_defaults() -> dict:
    data = dict(DEFAULTS)
    if os.path.exists(LAST_USED_FILE):
        try:
            with open(LAST_USED_FILE, encoding="utf-8") as f:
                data.update(json.load(f))
        except (json.JSONDecodeError, OSError):
            pass  # if the file is broken, fall back to config defaults
    return data


def save_last_used(data: dict) -> None:
    with open(LAST_USED_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
