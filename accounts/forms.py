from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.urls import reverse
from django.utils.translation import ugettext as _

from allauth.account.forms import SignupForm, LoginForm, ChangePasswordForm, ResetPasswordForm
from allauth.account.adapter import get_adapter
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Submit, Layout, Row, Field

from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name', 'need_mailing_news')

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Field('username', css_class='form-control'),
                Field('email', css_class='form-control'),
            ),
            Row(
                Field('first_name', css_class='form-control'),
                Field('last_name', css_class='form-control'),
            ),
            Row(
                Field('need_mailing_news', type="checkbox", css_class='form-check-input'),
            ),
            HTML(
                "<p><a class='button secondaryAction' href={url}>{text}</a></p>".format(
                    url=reverse('account_change_password'),
                    text=_('Change password.')
                )),
        )

        self.helper.add_input(Submit('submit', 'Edit profile', css_class='btn btn-success'))

class MyLoginForm(LoginForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Field('login', css_class='form-control'),
            ),
            Row(
                Field('password', css_class='form-control'),
            ),
        )

        # Add magic stuff to redirect back.
        self.helper.layout.append(
            HTML(
                "{% if redirect_field_value %}"
                "<input class='form-control' type='hidden' name='{{ redirect_field_name }}'"
                " value='{{ redirect_field_value }}' />"
                "{% endif %}"
            )
        )
        # Add password reset link.
        self.helper.layout.append(
            HTML(
                "<p><a class='button secondaryAction' href={url}>{text}</a></p>".format(
                    url=reverse('account_reset_password'),
                    text=_('Foggot password?')
                )
            )
        )
        # Add submit button like in original form.
        self.helper.layout.append(
            HTML(
                '<button class="btn btn-success" type="submit">'
                '%s</button>' % _('Log In')
            )
        )

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'form-control'
        self.helper.field_class = 'form-control'


class MySignupForm(SignupForm):
    username = forms.CharField(max_length=30, label='Username')
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=100, label='Last Name')

    # class Meta:
    #     model = get_user_model()
    #     fields = ('email', 'username', 'first_name', 'last_name')

    def custom_signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

    def save(self, request):
        adapter = get_adapter(request)
        new_user = adapter.new_user(request)
        adapter.save_user(request, new_user, self)
        self.custom_signup(request, new_user)

        return new_user

    def __init__(self, *args, **kwargs):
        super(MySignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Field('email', css_class='form-control'),
            ),
            Row(
                Field('first_name', css_class='form-control'),
                Field('last_name', css_class='form-control'),
            ),
            Row(
                Field('password1', css_class='form-control'),
                Field('password2', css_class='form-control'),
            ),
        )

        # self.helper.add_input(Submit('submit', 'Sign Up', css_class='btn btn-success'))

class MyChangePasswordForm(ChangePasswordForm):
    # pass
    def __init__(self, *args, **kwargs):
        super(MyChangePasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Field('oldpassword', css_class='form-control'),
            ),
            Row(
                Field('password1', css_class='form-control'),
                Field('password2', css_class='form-control'),
            ),
        )

        # self.helper.add_input(Submit('submit', 'Sign Up', css_class='btn btn-success'))

class MyResetPasswordForm(ResetPasswordForm):
    # pass
    def __init__(self, *args, **kwargs):
        super(MyResetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Field('email', css_class='form-control'),
            ),
        )

        # self.helper.add_input(Submit('submit', 'Reset My Password', css_class='btn btn-success'))
