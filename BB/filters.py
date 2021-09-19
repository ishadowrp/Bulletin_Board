import django_filters  # импортируем filterset, чем-то напоминающий знакомые дженерики
from django.forms import DateInput

class PostFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains', label='Author')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Title')
    date = django_filters.DateFilter(field_name='date_posted', widget=DateInput(attrs={'type': 'date'}), lookup_expr='icontains', label='Dated')
