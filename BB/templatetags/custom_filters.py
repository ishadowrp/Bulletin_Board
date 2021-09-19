from django import template

register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать и фильтры потеряются

LIST_OF_BAD_WORDS = ['лох', 'придурок', 'идиот']    # Список цензерируемых слов

@register.filter(name='censor')
def censor(value):
    if isinstance(value, str):  # проверяем, что value — это точно строка

        for word in LIST_OF_BAD_WORDS:
            value = value.replace(word, '*' * len(word))    # проверям в нижнем регистре
            value = value.replace(word.upper(), '*' * len(word))    # проверяем в верхнем регистре
            value = value.replace(word.capitalize(), '*' * len(word))   # проверяем с большой буквы

        return value
    else:
        raise ValueError(f'Нельзя цензурировать {type(value)}') #  в случае, если кто-то неправильно воспользовался нашим тегом, выводим ошибку

@register.filter
def fieldtype(obj):
    return obj.__class__.__name__