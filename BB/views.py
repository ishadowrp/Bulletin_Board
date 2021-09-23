# from django.shortcuts import render
# from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView  # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Мои библиотеку
from .models import Post, Category
# from .filters import PostFilter
from .forms import PostFormList, PostFormCreate, PostFormUpdate  # импортируем нашу форму списка

class SearchResultsListView(ListView):  # search
    model = Post
    context_object_name = 'posts'
    template_name = 'BB/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
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

class HomePageView(TemplateView):

    template_name = "flatpages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = len(Post.objects.all())
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


class AboutPageView(TemplateView):
    template_name = "flatpages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = len(Post.objects.all())
        i = 0
        list_fh = []
        list_sh = []
        for cat in Category.objects.all():
            i += 1
            if i <= len(Category.objects.all()) / 2:
                list_fh.append(cat)
            else:
                list_sh.append(cat)

        context['categories'] = Category.objects.all()
        context['cat_fh'] = list_fh
        context['cat_sh'] = list_sh
        return context


class ContactsPageView(TemplateView):
    template_name = "flatpages/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = len(Post.objects.all())
        i = 0
        list_fh = []
        list_sh = []
        for cat in Category.objects.all():
            i += 1
            if i <= len(Category.objects.all()) / 2:
                list_fh.append(cat)
            else:
                list_sh.append(cat)

        context['categories'] = Category.objects.all()
        context['cat_fh'] = list_fh
        context['cat_sh'] = list_sh
        return context


class PostList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'BB/posts.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через html-шаблон
    queryset = Post.objects.order_by('-date_posted')
    form_class = PostFormList

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = len(Post.objects.all())
        context['current_user'] = self.request.user
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не накосячил то сохраняем новое объявление
            form.save()
        return super().get(request, *args, **kwargs)

class PostDetail(DetailView):
    model = Post
    template_name = 'BB/post_detail.html'
    context_object_name = 'post'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user

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

class CategoryDetail(DetailView):
    model = Category
    template_name = 'BB/category_detail.html'
    context_object_name = 'category_detail'
    queryset = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts'] = Post.objects.filter(category=self.object)
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

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'BB/post_create.html'
    context_object_name = 'post_detail'
    form_class = PostFormCreate
    # permission_required = ('posts.add_post',)

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts'] = Post.objects.filter(category=self.object)
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

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'BB/post_update.html'
    context_object_name = 'post_detail'
    form_class = PostFormUpdate
    # permission_required = ('posts.add_post',)

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

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

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'BB/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('home')

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
