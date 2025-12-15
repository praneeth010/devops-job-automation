#!/usr/bin/env python3
import os
import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Environment variables (set via GitHub Secrets)
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

EMAIL_FROM = os.getenv("EMAIL_FROM")      # ratnalapraneeth@gmail.com
EMAIL_TO = os.getenv("EMAIL_TO")          # ratnalapraneeth@gmail.com
SMTP_HOST = os.getenv("SMTP_HOST")        # smtp.gmail.com
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER")        # ratnalapraneeth@gmail.com
SMTP_PASS = os.getenv("SMTP_PASS")        # Gmail App Password (SECRET)

QUERY = "DevOps Engineer 2 years OR 3 years"
LOCATION = "India"

def fetch_jobs():
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google_jobs",
        "q": QUERY,
        "location": LOCATION,
        "hl": "en",
        "api_key": SERPAPI_KEY
    }
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    return r.json().get("jobs_results", [])

def send_email(body):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = "Daily DevOps Engineer Jobs (2–3 Years) – India"
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USER, SMTP_PASS)
    server.send_message(msg)
    server.quit()

def main():
    jobs = fetch_jobs()
    lines = []
    for i, j in enumerate(jobs, 1):
        lines.append(f"{i}. {j.get('title', 'N/A')}")
        lines.append(f"   Company: {j.get('company_name', 'N/A')}")
        lines.append(f"   Location: {j.get('location', 'India')}")
        lines.append(f"   Apply: {j.get('apply_link') or j.get('link', 'N/A')}")
        lines.append("")

    body = "\n".join(lines) if lines else "No new DevOps jobs found in last 24 hours."
    send_email(body)

if __name__ == "__main__":
    main()