from django.http import HttpRequest
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Field, HTML, Column, MultiField

from .models import Post, Comment, Category
from django.forms.widgets import Textarea
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
    title = forms.CharField(max_length=150)
    content = forms.CharField(widget=CKEditorWidget())
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Post
        fields = ['title', 'category', 'content']
        labels = {'title': 'Title:', 'category': 'Category:', 'content': 'Content:'}

    def __init__(self, *args, **kwargs):
        super(PostFormCreate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Field('title', css_class='col-md-3 form-control'),
                Field('category', column="2", type="checkbox", css_class='form-check-input'),
            ),
            Row(
                Field('content', css_class='col-md-12'),
            )
        )

        self.helper.add_input(Submit('submit', 'Add post', css_class='btn btn-success'))

class PostFormUpdate(forms.ModelForm):
    # в класс мета как обычно надо написать модель по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    title = forms.CharField(max_length=150)
    content = forms.CharField(widget=CKEditorWidget())
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Post
        fields = ['title', 'category', 'content']
        labels = {'title': 'Title:', 'category': 'Category:', 'content': 'Content:'}

    def __init__(self, *args, **kwargs):
        super(PostFormUpdate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Field('title', css_class='col-md-3 form-control'),
                Field('category', type="checkbox", css_class='form-check-input'),
            ),
            Row(
                Field('content', css_class='col-md-12'),
            )
        )

        self.helper.add_input(Submit('submit', 'Edit post', css_class='btn btn-success'))

class CommentFormCreate(forms.ModelForm):

    content = forms.CharField(widget=Textarea)

    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': 'Comment:'}

    def __init__(self, *args, **kwargs):
        super(CommentFormCreate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Field('content', css_class='form-control'),
            ),
            HTML('<br>'),
        )

        self.helper.add_input(Submit('submit', 'Add comment', css_class='btn btn-success'))

class CommentFormList(forms.ModelForm):
    # в класс мета как обычно надо написать модель по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Comment
        fields = ['post', 'author', 'content', 'approved']
        labels = {'post': 'Post', 'author': 'Author:', 'content': 'Comment:', 'approved': 'Approved'}
