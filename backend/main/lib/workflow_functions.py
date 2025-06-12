import requests
import time
from main.lib.gmail_client import (
       send_plain_text_email,
       send_template_email
)
from main.template.email_template import html_template, order_mail_template
from decouple import config



def find_customer_by_email_or_phone(context):
    params = {"phone_number": context["phone"]}
    response = requests.get("http://localhost:8081/api/customer", params=params)
    context["user"] = response.json()
    return context


def fetch_most_recent_order(context):
    params = {"email": context["user"]["email"]}
    response = requests.get("http://localhost:8081/api/order", params=params)
    context["order"] = response.json()
    return context


def fetch_order_email(context):
    params = {"recipient_email": context["user"]["email"]}
    response = requests.get("http://localhost:8081/api/email", params=params)
    context["order_email"] = response.json()
    context["sent"] = False
    return context


def return_recipient_email_address(context):
    context["recipient_email"] = context["order_email"][0]["recipient_email"]
    return context


def send_order_confirmation_email(context):
    """Send order confirmation mail"""
    send_mail_with_template()
    context["order_email"] = {
            "id": 1,
            "subject": "Order Confirmation",
            "body": "Your order #1001 has been confirmed.",
            "sent_at": "2025-06-06T19:07:10.457702Z",
            "sender_email": "noreply@shop.com",
            "recipient_email": "unyimeudoh20@gmail.com",
            "status": "sent",
            "error_message": "",
            "type": "order",
            "context_id": 1001,
            "customer": 1
        }    
    return context


def send_mail_with_template():
        try:

            SMTP_USER = "unyimeudemy20@gmail.com"
            SMTP_PASSWORD = config("GMAIL_APP_PASSWORD")

            # send_plain_text_email(
            #         subject="Plain Text Test",
            #         body="This is a simple plain text email.",
            #         from_email=SMTP_USER,
            #         to_email="unyimeudoh20@gmail.com",
            #         smtp_user=SMTP_USER,
            #         smtp_password=SMTP_PASSWORD
            # )

            # Send HTML email using template


            send_template_email(
                    subject="Welcome to Our App",
                    template_str=order_mail_template,
                    context_dict={"name": "Unyime"},
                    from_email=SMTP_USER,
                    to_email="unyimeudoh20@gmail.com",
                    smtp_user=SMTP_USER,
                    smtp_password=SMTP_PASSWORD
            )

        except Exception as e:
               print(e)