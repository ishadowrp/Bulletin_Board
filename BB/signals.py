from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver  # импортируем нужный декоратор
from .models import Comment
from .tasks import email_notifying_new_comment, email_notifying_comment_approved

# в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция, и в отправители надо передать также модель
@receiver(post_save, sender=Comment)
def notify_users_new_comment(sender, instance, created, **kwargs):
    if created:
        usr_pk = instance.post.author.pk
        email_notifying_new_comment.apply_async([instance.id, created, usr_pk], countdown=5)

@receiver(post_save, sender=Comment)
def notify_users_comment_approved(sender, instance, created, **kwargs):
    if instance.approved:
        usr_pk = instance.author.pk
        email_notifying_comment_approved.apply_async([instance.id, created, usr_pk], countdown=5)
