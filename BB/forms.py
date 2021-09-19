from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget

# Создаём модельную форму
class PostFormList(forms.ModelForm):
    # в класс мета как обычно надо написать модель по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['author', 'category', 'title', 'content']
        labels = {'author': 'Author:', 'category': 'Category:', 'title': 'Title:', 'content': 'Content:'}

class PostFormCreate(forms.ModelForm):
    # в класс мета как обычно надо написать модель по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['author', 'category', 'title', 'content']
        labels = {'author': 'Author:', 'category': 'Category:', 'title': 'Title:', 'content': 'Content:'}
