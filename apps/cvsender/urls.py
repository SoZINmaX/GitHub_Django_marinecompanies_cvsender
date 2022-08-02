from django.urls import path
from . import views
from .views import Tableview

app_name = 'apps.cvsender'

urlpatterns = [
    path('company_list/', Tableview.as_view(), name='company_list'),
]