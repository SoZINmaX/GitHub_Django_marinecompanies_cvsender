from cProfile import label
from django import forms
from .models import UserSelectedCompany, Company, User
from django.contrib.auth import get_user_model
from django.forms import ModelChoiceField
from multiselectfield import MultiSelectFormField


User = get_user_model()

    
class UserSelectedCompanyForm(forms.ModelForm):
    class Meta:
        model = UserSelectedCompany
        fields = ['user', 'selected_companies', 'send_from_email', 'cv', 'text']
        widgets = {'text': forms.Textarea(attrs={'colls': 50})}
        labels = {'text': 'Pls write the content of Your e-mail here', 'cv': 'Pls upload Your CV here in PDF format'}
        
    def __init__(self, *args, company_list=None, user_selected=None, **kwargs):
        super().__init__(*args, **kwargs)
        CHOICES = Company.objects.filter(id__in = company_list)
        self.fields['selected_companies'] = MultiSelectFormField(choices = ( (x.id, x.name) for x in CHOICES ), label='Pls confirm Your selection')
        self.fields['user'] = ModelChoiceField(queryset=User.objects.filter(email = user_selected), initial=User.objects.get(email = user_selected), widget=forms.HiddenInput)
        self.fields['send_from_email'] = forms.CharField(initial=user_selected, label='Pls change Your e-mail for communication with companies if necessary')
        