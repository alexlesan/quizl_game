from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


class SendUserEmail:
    @staticmethod
    def send_registration_email(data):
        subject = "Thank you for registration"
        template = 'email/activate_account.html'
        message_html = render_to_string(template, data)
        email_from = settings.DEFAULT_FROM_EMAIL
        recipient_email = data['user'].email

        try:
            send_mail(subject, message_html, email_from, [recipient_email], fail_silently=False)
        except SMTPException as ex:
            print(f'Email was not sent. {ex}')
