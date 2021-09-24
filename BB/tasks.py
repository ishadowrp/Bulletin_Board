from celery import shared_task

from .models import Comment
from accounts.models import CustomUser
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


@shared_task
def email_notifying_new_comment(pk, created, usr_pk):

    full_url = ''.join(['http://', get_current_site(None).domain, ':8000'])
    instance = Comment.objects.get(pk=pk)
    if created:
        usr = CustomUser.objects.get(pk=usr_pk)
        html_content = render_to_string(
            'BB/subs_email.html',
            {
                'comment': instance,
                'usr': usr,
                'full_url': full_url,
                'created': created,
            }
        )

        msg = EmailMultiAlternatives(
            subject='New comment to your post!',
            body=f'Hello, {usr.first_name} {usr.last_name}. New comment on your post: '+instance.post_title,  #  это то же, что и message
            from_email='ilya.dinaburgskiy@yandex.ru',
            to=[f'{usr.email}'],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()  # отсылаем

@shared_task
def email_notifying_comment_approved(pk, created, usr_pk):

    full_url = ''.join(['http://', get_current_site(None).domain, ':8000'])
    instance = Comment.objects.get(pk=pk)
    if instance.approved:
        usr = CustomUser.objects.get(pk=usr_pk)
        html_content = render_to_string(
            'BB/subs_email.html',
            {
                'comment': instance,
                'usr': usr,
                'full_url': full_url,
                'created': created,
            }
        )
        msg = EmailMultiAlternatives(
            subject='Yours comment was be Approved!',
            body=f'Hello, {usr.first_name} {usr.last_name}. Your comment to post: '+instance.post_title+' was be approved!!',  #  это то же, что и message
            from_email='ilya.dinaburgskiy@yandex.ru',
            to=[f'{usr.email}'],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()  # отсылаем
