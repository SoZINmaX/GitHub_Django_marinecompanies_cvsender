from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import get_user_model, login, logout
from django.urls import reverse
from django.views import View
from django.views.generic import FormView, CreateView
from .forms import LoginForm, UserForm


User = get_user_model()


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'authentication/login.html'

    def form_valid(self, form):
        login(self.request, User.objects.get(email=form.cleaned_data['email']))
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.GET.get('next', '/')


class RegisterView(CreateView):
    form_class = UserForm
    success_url = '/'
    template_name = 'authentication/register.html'

    def form_valid(self, form):
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('accounts:user_login'))

# def login_view(request):
#     if request.method =='GET':
#         form = LoginForm()
#         return render(request, authentication/login.html, context={'form':form}) 
#     else:
#         form = LoginForm(request.POST) 
#         if form.is_valid():
#              user = User.objects.filter(email=username).first
#              if user and user.check_password(password):
#                  login(request, user)
#                  return HttpResponseRedirect(request.GET.get('next', ''))
#         else:
#             return render(request, 'authentication/login.html', context={'form':form})