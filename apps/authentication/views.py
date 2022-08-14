from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import get_user_model, login, logout
from django.urls import reverse
from django.views import View
from django.views.generic import FormView, CreateView
from .forms import LoginForm, UserForm
from django.contrib import messages


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
        result = super().form_valid(form)
        messages.add_message(self.request,
                             messages.SUCCESS,
                             'User successfully registered.')
        return result
    

class LogoutView(View):
     def get(self, request):
         logout(request)
         return HttpResponseRedirect(reverse('apps.authentication:login'))
     
def home(request):
    return render(request, 'authentication/home.html')