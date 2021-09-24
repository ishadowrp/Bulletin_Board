from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    need_mailing_news = models.BooleanField(default=False)

