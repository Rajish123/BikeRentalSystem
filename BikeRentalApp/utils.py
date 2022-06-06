from django.core.mail import send_mail
from django.conf import settings

class Util:
    @staticmethod
    def send_email(data):
        subject = data['email_subject']
        body = data['email_body']
        to = data['to_email']
        from_email = data['from_email']
        send_mail(subject,body,from_email,to,fail_silently=False)

