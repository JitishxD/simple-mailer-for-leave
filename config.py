"""Default values and settings. Edit once, then just press Enter later."""

DEFAULTS = {
    "name": "Your Name",
    "register_number": "24XXXXXXXX",
    "student_mobile": "9876543210",
    "place": "City, State",
    "departure_date": "29 October 2026",
    "departure_time": "5:00 P.M",
    "arrival_date": "16 November 2026",
    "arrival_time": "11:00 A.M",
    "father_name": "Father's Name",
    "parent_mobile": "9876543210",
    "address": "City, State",
    "reason": "Semester Break",
    "to": "recipient@gmail.com",
    "cc": "cc-recipient@example.com",
}

# (key, label shown to the user) — the order you'll be asked in
FIELDS = [
    ("to", "To (comma-separated)"),
    ("cc", "CC (comma-separated, type none to skip)"),
    ("reason", "Reason"),
    ("place", "Place of visit"),
    ("departure_date", "Departure date"),
    ("departure_time", "Departure time"),
    ("arrival_date", "Arrival date"),
    ("arrival_time", "Arrival time"),
    ("name", "Name"),
    ("register_number", "Register Number"),
    ("student_mobile", "Student mobile"),
    ("father_name", "Father's name"),
    ("parent_mobile", "Parent mobile"),
    ("address", "Address"),
]

SUBJECT_TEMPLATE = "{reason} - Permission For Leave"

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465  # SSL
ENV_FILE = ".env"
LAST_USED_FILE = "last_used.json"
