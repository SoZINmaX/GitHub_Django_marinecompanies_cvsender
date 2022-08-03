from .models import Company
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render



class Tableview(LoginRequiredMixin,TemplateView):
      
      template_name = 'cvsender/company_list.html'

      def get_context_data(self, **kwargs):
            contex = super(Tableview, self).get_context_data(**kwargs)
            contex['header'] = ['✔️', 'Name', 'Link', 'E-mail', 'Cadet_programm', 'Container', 'Bulk', 'Tanker', 'Chemical_tanker', 'Product_tanker', 'Gas_carrier', 'Lng', 'Lpg', 'Reefer', 'Ro-Ro', 'Heavy_lift', 'Passenger', 'Offshore', 'Ferry', 'Tug']
            contex['rows'] = Company.objects.all().values('name', 'link', 'email', 'cadet', 'container', 'bulk', 'tanker', 'chemical_tanker', 'product_tanker', 'gas_carrier', 'lng', 'lpg', 'reefer', 'ro_ro', 'heavy_lift', 'passenger', 'off_shore', 'ferry', 'tug').order_by('name')
            return contex
      
      
class InputView(FormView):
      
      template_name = 'cvsender/input_list.html' 
        
      def post(self, request):
            contex=request.POST.getlist('checks')
            return render(request, 'cvsender/input_list.html', context={'contex':contex})
      