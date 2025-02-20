import smtplib
from email.message import EmailMessage

def send_email(to_email, subject, body):
    sender_email = "varshini021nexether@gmail.com"
    sender_password = "Varshini@nex21"

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body, subtype="html")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:  # Gmail SMTP
            server.login(sender_email, sender_password)

            server.send_message(msg)
        return "Email sent successfully!"
    except Exception as e:
        return f"Error: {e}"

# Example Usage
print(send_email("recipient@example.com", "Test Subject", "<h1>Hello, World!</h1>"))
