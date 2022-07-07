import smtplib
import os
from email.message import EmailMessage

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

LATEST_FNAME = "latest.txt"
STABLE_FNAME = "stable.txt"

def send_message_to_self(subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = EMAIL
    msg.set_content(body)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.send_message(msg)

def handle_change(new_ip_addr):
    print("ip changed")
    send_message_to_self("New Public IP Addr", new_ip_addr)
    pass

def overwrite_file(f, text):
    f.seek(0)
    f.truncate()
    f.write(text + "\n")


dir_path = os.path.dirname(os.path.realpath(__file__))
latest_path = os.path.join(dir_path, LATEST_FNAME)
stable_path = os.path.join(dir_path, STABLE_FNAME)

# ensure files exist
with open(latest_path, "a+") as f:
    pass
with open(stable_path, "a+") as f:
    pass

with open(os.path.join(dir_path, LATEST_FNAME), "r") as f_latest:
    latest = f_latest.read().strip()
    with open(os.path.join(dir_path, STABLE_FNAME), "r+") as f_stable:
        stable = f_stable.read().strip()
        if latest != stable:
            overwrite_file(f_stable, latest)
            handle_change(latest)
