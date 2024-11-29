import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'developerharshraj@gmail.com'
    sender_password = 'Harsh2004@'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")


if __name__ == '__main__':
    recipient_email = 'candidate@example.com'
    subject = 'Upcoming Meeting with Electronics Inc.'
    body = '''
    Dear Candidate,

    We are pleased to inform you that we would like to schedule a meeting with you to discuss potential opportunities at Electronics Inc. 

    **Meeting Details:**
    - **Date:** September 15, 2024
    - **Time:** 10:00 AM (PST)
    - **Location:** Zoom (link will be provided in a follow-up email)

    **About Electronics Inc.:**
    Electronics Inc. is a leading innovator in the electronics industry, specializing in cutting-edge technology solutions and consumer electronics. Our mission is to drive progress through technology and deliver high-quality products to our customers worldwide.

    We look forward to speaking with you soon!

    Best regards,
    Harsh Raj
    HR Manager
    Electronics Inc.
    '''

    send_email(recipient_email, subject, body)
