from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives

User = get_user_model()


@shared_task
def send_invitation_email(user_id):
    user = User.objects.get(id=user_id)
    email = EmailMultiAlternatives(
        'This is subject of my email',
        'Text of email',
        settings.DEFAULT_FROM_EMAIL,
        [user.email]
    )

    email.attach_alternative(
        '<html>Visit <a href="/confirm-email/"> Confirm emil </a></html>',
        'text/html')

    email.send()