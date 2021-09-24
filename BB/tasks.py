from celery import shared_task

from .models import Comment, Post
from accounts.models import CustomUser
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
import datetime

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

@shared_task
def week_email_sending():
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=7)
    full_url = ''.join(['http://', get_current_site(None).domain, ':8000'])

    list_of_posts = Post.objects.filter(date_posted__range=(start_date, end_date))
    if len(list_of_posts) > 0:
        for u in CustomUser.objects.filter(need_mailing_news=True):
            html_content = render_to_string(
                'BB/subs_email_each_week.html',
                {
                    'news': list_of_posts,
                    'usr': u,
                    'full_url': full_url,
                }
            )
            msg = EmailMultiAlternatives(
                subject=f'Hello, {u.first_name} {u.last_name}. We have prepared a digest of articles for a week from our portal!',
                body='',
                # это то же, что и message
                from_email='ilya.dinaburgskiy@yandex.ru',
                to=[f'{u.email}'],  # это то же, что и recipients_list
            )
            msg.attach_alternative(html_content, "text/html")  # добавляем html

            msg.send()  # отсылаем
