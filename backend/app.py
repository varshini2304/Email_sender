import smtplib
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    raise ValueError("❌ EMAIL_ADDRESS or EMAIL_PASSWORD not set in .env file.")

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.json
    recipient = data.get("to")
    subject = data.get("subject")
    body = data.get("body")

    if not recipient or not subject or not body:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        print(f"📧 Sending email to: {recipient}")  # Debugging log
        message = f"From: {EMAIL_ADDRESS}\nTo: {recipient}\nSubject: {subject}\n\n{body}"

        # Use 'with' to ensure proper closing of the connection
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient, message)

        print("✅ Email sent successfully!")
        return jsonify({"message": "Email sent successfully!"})

    except Exception as e:
        print(f"❌ Error: {e}")  # Logs the real error
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
