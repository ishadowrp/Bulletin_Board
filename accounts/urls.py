from django.urls import path
from .views import AccountUpdateView

urlpatterns = [
    path('signin/', AccountUpdateView.as_view(), name='signin'),
]
