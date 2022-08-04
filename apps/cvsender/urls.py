from django.urls import path
from .views import Tableview, RegisterEntry
from . import views

app_name = 'apps.cvsender'

urlpatterns = [
    path('company_list/', Tableview.as_view(), name='company_list'),
    path('input_list/', RegisterEntry.as_view(), name='input_list')
]