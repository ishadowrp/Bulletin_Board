from django.urls import path
from .views import SignupPageView, LoginPage

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('login/', LoginPage.as_view(), name='login'),
]
