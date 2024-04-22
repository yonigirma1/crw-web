from django.template.loader import render_to_string
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from crw_school.settings import env


class EmailSender:
    @staticmethod
    def send_email(template_name, subject, contact):
        message = render_to_string(template_name, contact)
        mail = Mail(from_email=env('SENDER_EMAIL'), to_emails=env('RECEIVERS_EMAIL').split(','),
                    subject=subject, html_content=message)
        try:
            send_grid = SendGridAPIClient(env('SENDGRID_API_KEY'))
            send_grid.send(mail)
            return True
        except:
            return False
