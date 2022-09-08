from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives


User = get_user_model()
        
        
@shared_task   
def send_email(companies, text, send_from_email, cv): 
    for company in companies:
        companies_selected = company.get('email')
        subject = "CV"   
        from_email = settings.DEFAULT_FROM_EMAIL
        to = companies_selected
        text_content  = str(text)+str(send_from_email)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_file(cv)
        msg.send()