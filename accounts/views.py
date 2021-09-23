from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser as User

from .forms import CustomUserChangeForm

from allauth.account.views import LoginView, SignupView, LogoutView, ConfirmEmailView, PasswordChangeView, PasswordResetView
from BB.models import Category


class MyPasswordResetView(PasswordResetView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        i = 0
        list_fh = []
        list_sh = []
        for cat in Category.objects.all():
            i += 1
            if i <= len(Category.objects.all())/2:
                list_fh.append(cat)
            else:
                list_sh.append(cat)

        context['categories'] = Category.objects.all()
        context['cat_fh'] = list_fh
        context['cat_sh'] = list_sh
        return context

class MyPasswordChangeView(PasswordChangeView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        i = 0
        list_fh = []
        list_sh = []
        for cat in Category.objects.all():
            i += 1
            if i <= len(Category.objects.all())/2:
                list_fh.append(cat)
            else:
                list_sh.append(cat)

        context['categories'] = Category.objects.all()
        context['cat_fh'] = list_fh
        context['cat_sh'] = list_sh
        return context


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    context_object_name = 'user'
    template_name = 'account/signin.html'
    form_class = CustomUserChangeForm
    success_url = '/'

    def get_object(self, **kwargs):
        # id = self.kwargs.get('pk')
        return User.objects.get(id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        i = 0
        list_fh = []
        list_sh = []
        for cat in Category.objects.all():
            i += 1
            if i <= len(Category.objects.all())/2:
                list_fh.append(cat)
            else:
                list_sh.append(cat)

        context['categories'] = Category.objects.all()
        context['cat_fh'] = list_fh
        context['cat_sh'] = list_sh
        return context


class SignupPageView(SignupView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        i = 0
        list_fh = []
        list_sh = []
        for cat in Category.objects.all():
            i += 1
            if i <= len(Category.objects.all())/2:
                list_fh.append(cat)
            else:
                list_sh.append(cat)

        context['categories'] = Category.objects.all()
        context['cat_fh'] = list_fh
        context['cat_sh'] = list_sh
        return context


class LoginPageView(LoginView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        i = 0
        list_fh = []
        list_sh = []
        for cat in Category.objects.all():
            i += 1
            if i <= len(Category.objects.all())/2:
                list_fh.append(cat)
            else:
                list_sh.append(cat)

        context['categories'] = Category.objects.all()
        context['cat_fh'] = list_fh
        context['cat_sh'] = list_sh
        return context


class LogoutPageView(LogoutView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        i = 0
        list_fh = []
        list_sh = []
        for cat in Category.objects.all():
            i += 1
            if i <= len(Category.objects.all())/2:
                list_fh.append(cat)
            else:
                list_sh.append(cat)

        context['categories'] = Category.objects.all()
        context['cat_fh'] = list_fh
        context['cat_sh'] = list_sh
        return context

class ConfirmEmailPageView(ConfirmEmailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        i = 0
        list_fh = []
        list_sh = []
        for cat in Category.objects.all():
            i += 1
            if i <= len(Category.objects.all())/2:
                list_fh.append(cat)
            else:
                list_sh.append(cat)

        context['categories'] = Category.objects.all()
        context['cat_fh'] = list_fh
        context['cat_sh'] = list_sh
        return context
