import smtplib
import ssl
import certifi
from email.message import EmailMessage
from jinja2 import Template


def send_plain_text_email(subject, body, from_email, to_email, smtp_user, smtp_password):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    context = ssl.create_default_context(cafile=certifi.where())

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(smtp_user, smtp_password)
        server.send_message(msg)


def send_template_email(subject, template_str, context_dict, from_email, to_email, smtp_user, smtp_password):
    # Render HTML using Jinja2
    template = Template(template_str)
    html_content = template.render(context_dict)

    msg = EmailMessage()
    msg.set_content("This is a fallback plain-text message.")
    msg.add_alternative(html_content, subtype="html")
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    context = ssl.create_default_context(cafile=certifi.where())

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(smtp_user, smtp_password)
        server.send_message(msg)


