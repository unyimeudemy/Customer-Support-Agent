
no_confirmation_email_json = {
    "intent": "NO_CONFIRMATION_EMAIL",
    "complaint_type": "Missing order confirmation",
    "steps": [
        {"action": "find_customer_by_email_or_phone"},
        {"action": "fetch_most_recent_order"},
        {
            "action": "check_order_status",
            "expected_status": "successful"
        },
        {"action": "verify_email_sent"},
        {
            "decision": [
                {
                    "if": "email_sent",
                    "then": [
                        {"action": "check_email_recipient"},
                        {"action": "notify_user_where_email_was_sent"}
                    ]
                },
                {
                    "else": {
                        "action": "send_confirmation_email"
                    }
                }
            ]
        }

    ]
}