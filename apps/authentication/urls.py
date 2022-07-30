from django.urls import path

from .views import LoginView, LogoutView, RegisterView

app_name = 'apps.authentication'

urlpatterns = [
    path('login/', LoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('register/', RegisterView.as_view(), name='user-register')
]