import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, recipient):
    # Set up the SMTP server
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_username'
    smtp_password = 'your_password'

    # Create a multipart message
    message = MIMEMultipart()
    message['From'] = smtp_username
    message['To'] = recipient
    message['Subject'] = subject

    # Add the body to the message
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)

# Example usage
subject = 'Daily Journal Entry'
body = 'Today, I accomplished...'
recipient = 'example@example.com'

send_email(subject, body, recipient)
