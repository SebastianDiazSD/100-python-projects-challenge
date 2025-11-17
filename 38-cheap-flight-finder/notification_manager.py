# notification_manager.py
# Handles email notifications (Gmail) and optional Twilio SMS/WhatsApp.

import os
import smtplib
from email.message import EmailMessage

try:
    from twilio.rest import Client as TwilioClient
except Exception:
    TwilioClient = None


class NotificationManager:
    def __init__(self):
        # Email config
        self.smtp_address = os.environ.get("EMAIL_PROVIDER_SMTP_ADDRESS", "smtp.gmail.com")
        self.email = os.environ.get("MY_EMAIL")
        self.email_password = os.environ.get("MY_EMAIL_PASSWORD")

        if not all([self.email, self.email_password]):
            print("Warning: Email credentials not found in environment. Email sending will fail unless configured.")

        # Twilio config (optional)
        self.twilio_sid = os.environ.get("TWILIO_SID")
        self.twilio_auth = os.environ.get("TWILIO_AUTH_TOKEN")
        self.twilio_virtual_number = os.environ.get("TWILIO_VIRTUAL_NUMBER")
        self.twilio_verified_number = os.environ.get("TWILIO_VERIFIED_NUMBER")
        self.whatsapp_number = os.environ.get("TWILIO_WHATSAPP_NUMBER")

        self.twilio_client = None
        if self.twilio_sid and self.twilio_auth and TwilioClient:
            try:
                self.twilio_client = TwilioClient(self.twilio_sid, self.twilio_auth)
            except Exception as ex:
                print(f"Twilio init failed: {ex}")
                self.twilio_client = None

    def send_whatsapp(self, message_body: str):
        if not self.twilio_client:
            print("Twilio not configured — cannot send WhatsApp message.")
            return
        try:
            msg = self.twilio_client.messages.create(
                from_=f"whatsapp:{self.whatsapp_number}",
                body=message_body,
                to=f"whatsapp:{self.twilio_verified_number}"
            )
            print(f"WhatsApp sent, sid: {msg.sid}")
        except Exception as ex:
            print(f"Failed to send WhatsApp: {ex}")

    def send_emails(self, email_list, email_body: str, subject: str = "Low Price Flight Alert!"):
        """
        Sends a simple email to each address in email_list using SMTP (STARTTLS).
        Uses EmailMessage for clean formatting.
        """
        if not all([self.email, self.email_password]):
            print("Email not configured. Set MY_EMAIL and MY_EMAIL_PASSWORD in .env (use Gmail App Password).")
            return

        msg = EmailMessage()
        msg["From"] = self.email
        msg["Subject"] = subject
        msg.set_content(email_body)

        # connect to SMTP server
        try:
            with smtplib.SMTP(self.smtp_address, 587, timeout=20) as connection:
                connection.ehlo()
                connection.starttls()
                connection.login(self.email, self.email_password)
                for addr in email_list:
                    msg["To"] = addr
                    connection.send_message(msg)
                    del msg["To"]  # remove header for next iteration
            print(f"Emails sent to {len(email_list)} recipients.")
        except Exception as ex:
            print(f"Failed to send emails: {ex}")
