"""Input helpers: pressing Enter keeps the default."""

# Fields where typing "none" clears the value instead of using the default
SKIPPABLE_FIELDS = {"cc"}


def ask(label: str, key: str, default: str = "") -> str:
    shown = f" [{default}]" if default else ""
    value = input(f"{label}{shown}: ").strip()
    if key in SKIPPABLE_FIELDS and value.lower() == "none":
        return ""
    return value or default


def confirm(question: str, default: bool = False) -> bool:
    hint = "Y/n" if default else "y/N"
    answer = input(f"{question} ({hint}): ").strip().lower()
    if not answer:
        return default
    return answer in ("y", "yes")


def collect_details(fields, defaults: dict) -> dict:
    print("Press Enter to keep the value shown in [brackets].\n")
    return {key: ask(label, key, defaults.get(key, "")) for key, label in fields}
