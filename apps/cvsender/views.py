from .models import Company
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserSelectedCompanyForm
from django.contrib.auth import get_user_model


User = get_user_model()


class Tableview(LoginRequiredMixin,TemplateView):
      
      template_name = 'cvsender/company_list.html'

      def get_context_data(self, **kwargs):
            contex = super(Tableview, self).get_context_data(**kwargs)
            contex['header'] = ['✔️', 'Name', 'Link', 'E-mail', 'Cadet_programm', 'Container', 'Bulk', 'Tanker', 'Chemical_tanker', 'Product_tanker', 'Gas_carrier', 'Lng', 'Lpg', 'Reefer', 'Ro-Ro', 'Heavy_lift', 'Passenger', 'Offshore', 'Ferry', 'Tug', 'ID']
            contex['rows'] = Company.objects.all().values('name', 'link', 'email', 'cadet', 'container', 'bulk', 'tanker', 'chemical_tanker', 'product_tanker', 'gas_carrier', 'lng', 'lpg', 'reefer', 'ro_ro', 'heavy_lift', 'passenger', 'off_shore', 'ferry', 'tug', 'id').order_by('name')
            return contex


class RegisterEntry(CreateView):
      form_class = UserSelectedCompanyForm
      template_name = 'cvsender/input_list.html' 
      success_url = '/'
      
      def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            kwargs['company_list'] =self.request.GET.getlist('checks')
            kwargs['user_selected'] = self.request.user.email
            return kwargs
      