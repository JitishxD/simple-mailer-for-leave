# Leave Mailer

A small command-line tool that writes and sends leave-permission emails from your Gmail account.
It asks for each detail and shows a default value; press **Enter** to keep it.
Before sending, it shows the full mail and asks you to confirm.

No external libraries needed. It uses only the Python standard library.

---

## Features

- Asks for every field (dates, times, reason, recipients, and so on), with Enter to keep the default
- Remembers your last-used values, so next time you only change what's different
- The subject follows the reason, e.g. `[Semester Break] Permission For Leave`
- Default **To:** `recipient@gmail.com`, default **CC:** `cc-recipient@example.com`
- Shows the full mail before sending and asks for confirmation
- Sends through Gmail SMTP using an App Password (your real password is never stored)

---

## Project Structure

```
leave_mailer/
├── config.py        # default values, field labels, SMTP settings
├── template.py      # mail body and subject format
├── prompts.py       # input helpers (Enter keeps the default)
├── storage.py       # saves/loads last-used values (last_used.json)
├── auth.py          # reads your Gmail login from .env
├── mailer.py        # builds and sends the email
├── main.py          # runs everything in order
├── .env             # your Gmail address and app password (keep private)
├── .gitignore
└── README.md
```

---

## Requirements

- Python **3.9 or newer**
- A Gmail account with **2-Step Verification** turned on

Check your Python version:
```
python --version
```

---

## Gmail Setup (one time)

Gmail won't accept your normal password from a script. You need an **App Password**.

1. **Turn on 2-Step Verification**
   Go to https://myaccount.google.com/security and turn it on under
   *"How you sign in to Google"*.

2. **Create an App Password**
   Go to https://myaccount.google.com/apppasswords, enter a name such as
   `Leave Mailer`, and click **Create**. Copy the 16-character code
   (e.g. `abcd efgh ijkl mnop`).

3. **Create a `.env` file** in the project folder:
   ```
   GMAIL_ADDRESS=yourname@gmail.com
   GMAIL_APP_PASSWORD=abcd efgh ijkl mnop
   ```
   Spaces in the app password are fine; the program removes them.

   If you skip this step, the program will ask for your email and app password each time you run it.

> **Note:** If you use a college Google account, the admin may have turned off App Passwords.
> In that case, use a personal `@gmail.com` account.

---

## Usage

```
cd leave_mailer
python main.py
```

Example session:
```
Press Enter to keep the value shown in [brackets].

To (comma-separated) [recipient@gmail.com]:
CC (comma-separated, blank for none) [cc-recipient@example.com]:
Reason [Semester Break]:
Place of visit [City, State]:
Departure date [29 October 2026]: 30 October 2026
Departure time [5:00 P.M]:
Arrival date [16 November 2026]:
Arrival time [11:00 A.M]:
...
============================================================
PREVIEW
============================================================
From    : Your Name <yourname@gmail.com>
To      : recipient@gmail.com
Cc      : cc-recipient@example.com
Subject : [Semester Break] Permission For Leave
============================================================
Respected sir,
...
============================================================
Send this mail? (y/N): y
Mail sent successfully.
```

---

## Customizing

| What you want to change          | Where to edit                       |
|----------------------------------|-------------------------------------|
| Default values (name, numbers…)  | `DEFAULTS` in `config.py`           |
| Order of questions / labels      | `FIELDS` in `config.py`             |
| Subject format                   | `SUBJECT_TEMPLATE` in `config.py`   |
| Mail wording / layout            | `BODY_TEMPLATE` in `template.py`    |

**About defaults:** After your first run, the values you entered are saved in
`last_used.json` and become the new defaults. Delete that file to go back to the
defaults in `config.py`.

---

## Building an EXE

If you want a standalone `.exe` you can run without installing Python:

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Open `auth.py` and **hardcode** your credentials:
   ```python
   # Uncomment these two lines and fill in your values:
   address = "yourname@gmail.com"
   password = "abcd efgh ijkl mnop"

   # Comment out these two lines:
   # address = os.environ.get("GMAIL_ADDRESS") or input("Your Gmail address: ").strip()
   # password = os.environ.get("GMAIL_APP_PASSWORD") or getpass("Gmail App Password: ")
   ```

3. Build the exe:
   ```
   pyinstaller --icon=icon.ico --onefile main.py
   ```

4. The exe will be in the `dist/` folder. Run it directly — no Python or `.env` needed.

> **⚠️ Warning:** Your credentials are embedded inside the exe. Don't share it publicly.
> After building, **undo the changes** in `auth.py` so you don't accidentally commit real credentials.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `Login failed` / `SMTPAuthenticationError` | Use an **App Password**, not your normal password. Check `.env` for typos. |
| App Passwords page says "not available" | Turn on 2-Step Verification first, or use a personal Gmail account (college accounts may block it). |
| Old defaults keep showing | Delete `last_used.json`. |
| Mail lands in spam | Ask the recipient to mark it "Not spam" once. |
| EXE icon is cached | Windows caches icons. Delete the cache and restart Explorer: `del "%LOCALAPPDATA%\IconCache.db"` and `del "%LOCALAPPDATA%\Microsoft\Windows\Explorer\iconcache*"`, then restart Explorer (`taskkill /f /im explorer.exe & start explorer`). |

---

## Security

- **Never share or commit `.env`.** It's already in `.gitignore`.
- Anyone with your App Password can send mail as you. If it leaks, delete it from
  https://myaccount.google.com/apppasswords and create a new one.
- Your real Google password is never used or stored by this tool.
