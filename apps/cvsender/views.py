
from .models import Company
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserSelectedCompanyForm
from django.contrib.auth import get_user_model
from .tasks import send_email
from django.contrib import messages
import json
from django.core.serializers.json import DjangoJSONEncoder


User = get_user_model()


class Tableview(LoginRequiredMixin,TemplateView):
      
      template_name = 'cvsender/company_list.html'
      
      def get_context_data(self, **kwargs):

            try:
                  if self.request.GET.getlist('dropdown'):
                        name = self.request.GET.getlist('dropdown')
                  else:
                        name = name=['name']
            finally: 
                  
                  if name[0] == 'name':
                        contex = super(Tableview, self).get_context_data(**kwargs)
                        contex['header'] = ['✔️', 'Name', 'Adress', 'Website info', 'Email', 'Phone number', 'Cadet program', 'Container', 'Bulk', 'Tanker', 'Gas carrier', 'Reefer', 'Ro-Ro', 'Heavy_lift', 'Passenger', 'Offshore', 'Yachts', 'Fishing', 'Tug', 'Ferry', 'ID']
                        contex['rows'] = Company.objects.all().values('name', 'adress', 'website_info', 'email', 'phone_number', 'cadet_program', 'container', 'bulk', 'tanker', 'gas_carrier', 'reefer', 'ro_ro', 'heavy_lift', 'passenger', 'off_shore', 'yachts', 'fishing', 'tug', 'ferry', 'id').order_by(name[0]) 
                                   
                  elif name[0] == 'Selct filter': 
                        contex = super(Tableview, self).get_context_data(**kwargs)
                        contex['header'] = ['✔️', 'Name', 'Adress', 'Website info', 'Email', 'Phone number', 'Cadet program', 'Container', 'Bulk', 'Tanker', 'Gas carrier', 'Reefer', 'Ro-Ro', 'Heavy_lift', 'Passenger', 'Offshore', 'Yachts', 'Fishing', 'Tug', 'Ferry', 'ID']
                        contex['rows'] = Company.objects.all().values('name', 'adress', 'website_info', 'email', 'phone_number', 'cadet_program', 'container', 'bulk', 'tanker', 'gas_carrier', 'reefer', 'ro_ro', 'heavy_lift', 'passenger', 'off_shore', 'yachts', 'fishing', 'tug', 'ferry', 'id').order_by('name')
                  else:
                        contex = super(Tableview, self).get_context_data(**kwargs)
                        contex['header'] = ['✔️', 'Name', 'Adress', 'Website info', 'Email', 'Phone number', 'Cadet program', 'Container', 'Bulk', 'Tanker', 'Gas carrier', 'Reefer', 'Ro-Ro', 'Heavy_lift', 'Passenger', 'Offshore', 'Yachts', 'Fishing', 'Tug', 'Ferry', 'ID']
                        contex['rows'] = Company.objects.all().values('name', 'adress', 'website_info', 'email', 'phone_number', 'cadet_program', 'container', 'bulk', 'tanker', 'gas_carrier', 'reefer', 'ro_ro', 'heavy_lift', 'passenger', 'off_shore', 'yachts', 'fishing', 'tug', 'ferry', 'id').order_by(name[0]).reverse()    
                                        
            return contex

class RegisterEntry(LoginRequiredMixin, CreateView):
      form_class = UserSelectedCompanyForm
      template_name = 'cvsender/input_list.html' 
      success_url = '/'
      
      def send_emails(self):
            
            id = self.object.user_id
            companies = list(self.object.selected_companies.all().values('email'))
            text = self.object.text
            send_from_email = self.object.send_from_email
            cv = self.object.cv.path
            
            send_email.delay(companies, text, send_from_email, cv)
            
      def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            kwargs['company_list'] =self.request.GET.getlist('checks')
            kwargs['user_selected'] = self.request.user.email
            return kwargs
      
      def form_valid(self, form):
            """If the form is valid, save the associated model."""
            self.object = form.save()
            res = super().form_valid(form)
            self.send_emails()
            messages.add_message(self.request,messages.SUCCESS,'Message Sent. Thank You for using this app')
            return res
  