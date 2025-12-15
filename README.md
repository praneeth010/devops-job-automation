DevOps Job Automation – Gmail Setup (SAFE)

This project emails daily DevOps Engineer jobs (2–3 years) in India at 11:30 AM IST.

IMPORTANT:
- Do NOT put passwords in code.
- Use GitHub Secrets only.

GitHub Secrets to add:
EMAIL_FROM = ratnalapraneeth@gmail.com
EMAIL_TO   = ratnalapraneeth@gmail.com
SMTP_HOST  = smtp.gmail.com
SMTP_PORT  = 587
SMTP_USER  = ratnalapraneeth@gmail.com
SMTP_PASS  = <GMAIL APP PASSWORD>
SERPAPI_KEY= <YOUR SERPAPI KEY>

Steps:
1. Create GitHub repo
2. Upload this folder
3. Add secrets
4. Enable GitHub Actions