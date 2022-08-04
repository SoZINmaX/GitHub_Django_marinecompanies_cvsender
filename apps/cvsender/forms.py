from urllib import request
from django import forms
from .models import UserSelectedCompany, Company
from django.contrib.auth import get_user_model
from django.forms import ChoiceField, ModelChoiceField, ModelMultipleChoiceField


User = get_user_model()


class UserSelectedCompanyForm(forms.ModelForm):
    class Meta:
        model = UserSelectedCompany
        fields = ['user', 'selected_companies', 'send_from_email', 'cv', 'text']
        widgets = {'text': forms.Textarea(attrs={'colls': 80})}
        
    def __init__(self, *args, company_list=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['selected_companies'] = ModelMultipleChoiceField(queryset=Company.objects.filter(id__in=company_list))
        