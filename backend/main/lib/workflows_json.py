
no_confirmation_email_json = {
    "intent": "NO_CONFIRMATION_EMAIL",
    "complaint_type": "Missing order confirmation",
    "steps": [
        {"action": "find_customer_by_email_or_phone"},
        {"action": "fetch_most_recent_order"},
        {"action": "fetch_order_email"},
        {
            "decision": [
                {
                    "if": "sent",
                    "then": [
                        {"action": "return_recipient_email_address"},
                    ]
                },
                {
                    "else": [
                        {"action": "send_order_confirmation_email"}
                    ]
                }
            ]
        }

    ]
}