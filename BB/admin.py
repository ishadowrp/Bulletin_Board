from django.contrib import admin
from .models import Category, Post, Comment, PostCategory

class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1

class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    inlines = (PostCategoryInline,)
    list_display = ['pk', 'title', 'author', 'in_category', 'date_posted']
    list_display_links = ('pk', 'title',)
    list_filter = ('title', 'author', 'date_posted') # добавляем примитивные фильтры в нашу админку
    search_fields = ('title', 'author') # тут всё очень похоже на фильтры из запросов в базу

class CommentAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['pk', 'post_title', 'author', 'date_posted', 'approved']
    list_display_links = ('pk',)
    list_filter = ('post__title', 'author', 'date_posted', 'approved')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('post__title', 'author')  # тут всё очень похоже на фильтры из запросов в базу


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)


