from django.urls import path

from .views import LoginView, LogoutView, RegisterView
from . import views

app_name = 'apps.authentication'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', views.home, name='home')
]