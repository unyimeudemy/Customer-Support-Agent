
from celery import shared_task
from decouple import config
import imaplib
import email
from email.header import decode_header
import os
import django
from datetime import datetime, timedelta


class GmailSession:
    def __init__(self):
        self.EMAIL = "unyimeudemy20@gmail.com"
        self.APP_PASSWORD = config("GMAIL_APP_PASSWORD")
        self.IMAP_SERVER = "imap.gmail.com"
        self.mail = None

    def connect(self):
        if self.mail is None:
            self.mail = imaplib.IMAP4_SSL(self.IMAP_SERVER)
            self.mail.login(self.EMAIL, self.APP_PASSWORD)
            self.mail.select("inbox")
            print("IMAP session established.")

    def disconnect(self):
        if self.mail is not None:
            self.mail.logout()
            self.mail = None
            print("IMAP session closed.")

    def check_gmail_inbox(self):

        try:

            seven_days_ago = (datetime.utcnow() - timedelta(days=7)).strftime("%Y/%m/%d")
            search_query = f'X-GM-RAW "category:primary is:unread after:{seven_days_ago}"'

            status, messages = self.mail.search('UTF8', search_query)

            if status != "OK" or not messages[0]:
                return {"message": "No unseen messages."}

            latest_email_id = messages[0].split()[-1]
            status, data = self.mail.fetch(latest_email_id, "(RFC822)")
            if status != "OK":
                return {"message": "Failed to fetch email."}

            msg = email.message_from_bytes(data[0][1])

            # Get Subject
            subject, encoding = decode_header(msg.get("Subject", "No Subject"))[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8")

            # Get From
            from_ = msg.get("From", "Unknown Sender")

            # Get To
            to_ = msg.get("To", "Unknown Recipient")

            # Get Body
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain" and not part.get("Content-Disposition"):
                        body = part.get_payload(decode=True).decode(errors="ignore")
                        break
            else:
                body = msg.get_payload(decode=True).decode(errors="ignore")

            # Mark it as read
            self.mail.store(latest_email_id, '+FLAGS', '\\Seen')
            # mail.logout()

            return {
                "subject": subject.strip(),
                "body": body.strip(),
                "from": from_,
                "to": to_,
            }

        except Exception as e:
            return {"error": str(e)}

