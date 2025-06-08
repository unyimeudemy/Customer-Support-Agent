import requests
import time


def find_customer_by_email_or_phone(context):
    params = {"phone_number": context["phone"]}
    response = requests.get("http://localhost:8081/api/customer", params=params)
    context["user"] = response.json()

    # time.sleep(1)

    # context["user"] = {
    #     "id": 1,
    #     "first_name": "unyime",
    #     "last_name": "udoh",
    #     "email": "unyimeudoh20@gmail.com",
    #     "phone_number": "+2347046886451",
    #     "account_status": "active",
    #     "created_at": "2025-06-06T18:51:55.424214Z",
    #     "updated_at": "2025-06-06T18:51:55.424214Z"
    # }
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
    context["sent"] = True
    return context


def return_recipient_email_address(context):
    context["recipient_email"] = context["order_email"][0]["recipient_email"]
    return context


def send_order_confirmation_email(context):
    time.sleep(1)
    """Send order confirmation mail"""
    context["sent"] = True
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