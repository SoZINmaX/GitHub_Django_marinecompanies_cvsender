from django.urls import path

from .views import LoginView, LogoutView, RegisterView

app_name = 'apps.authentication'

urlpatterns = [
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('register/', RegisterView.as_view(), name='user_register'),
]