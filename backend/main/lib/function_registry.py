from main.lib.workflow_functions import (
    return_recipient_email_address,
    fetch_most_recent_order,
    fetch_order_email,
    find_customer_by_email_or_phone,
    send_order_confirmation_email
)


FUNCTION_REGISTRY = {
    "find_customer_by_email_or_phone": find_customer_by_email_or_phone,
    "fetch_most_recent_order": fetch_most_recent_order,
    "return_recipient_email_address": return_recipient_email_address,
    "fetch_order_email": fetch_order_email,
    "send_order_confirmation_email": send_order_confirmation_email,
}