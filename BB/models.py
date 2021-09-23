from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    rating = models.IntegerField(default=0)

    @property
    def in_category(self):
        list_of_category = [category.name for category in self.category.all()]
        return list_of_category

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.content[:125]+'...'

    def get_absolute_url(self):  # добавим абсолютный путь чтобы после создания нас перебрасывало на страницу с новостью
        return f'/posts/{self.id}'

    def __str__(self):
        return f'{self.title}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    approved = models.BooleanField(default=False)

    @property
    def post_title(self):
        return self.post.title

