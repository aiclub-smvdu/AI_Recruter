import smtplib
from email.mime.text import MIMEText

def send_messages(candidates):
    for candidate in candidates.itertuples():
        msg = MIMEText(f"Dear {candidate.name}, you have been shortlisted.")
        msg['Subject'] = 'Interview Invitation'
        msg['From'] = 'your_email@example.com'
        msg['To'] = candidate.email

        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_password')
            server.send_message(msg)
