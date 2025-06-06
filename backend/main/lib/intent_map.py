from collections import defaultdict


INTENT_MAP = defaultdict(list)

INTENT_MAP["NO_CONFIRMATION_EMAIL"] = [
    "I placed an order and have not received a confirmation email.",
    "It's been hours and I still haven’t gotten my order confirmation.",
    "I haven’t received any email about my recent purchase.",
    "No confirmation email came after I ordered.",
    "I ordered something but didn’t get a confirmation email.",
    "Can you check if my order confirmation email was sent?"
]