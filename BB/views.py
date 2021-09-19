# from django.shortcuts import render
# from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.contrib.auth.decorators import login_required

# Мои библиотеку
from .models import Post, Category
# from .filters import PostFilter
from .forms import PostFormList, PostFormCreate  # импортируем нашу форму списка

class PostList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'BB/posts.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через html-шаблон
    queryset = Post.objects.order_by('-date_posted')
    form_class = PostFormList

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

        print(context)

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

class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    template_name = 'BB/post_create.html'
    context_object_name = 'post_detail'
    form_class = PostFormCreate
    # permission_required = ('news.add_post',)

class CategoryListWidget(ListView):
    model = Category  # указываем модель, объекты которой мы будем выводить
    template_name = 'BB/categories-widget.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'categories'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через html-шаблон

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
