from django.db import models
from apps.authentication.models import User

class Company(models.Model):
    
    name = models.CharField("name", max_length=200)
    link = models.URLField("link", max_length=200, null=True)
    email = models.EmailField("email", max_length = 200, null=True)
    cadet = models.BooleanField("cadet", default=False)
    container = models.BooleanField("container", default=False)
    bulk = models.BooleanField("bulk", default=False)
    tanker = models.BooleanField("tanker", default=False)
    chemical_tanker = models.BooleanField("chemical_tanker", default=False)
    product_tanker = models.BooleanField("product_tanker", default=False)
    gas_carrier = models.BooleanField("gas_carrier", default=False)
    lng = models.BooleanField("lng", default=False)
    lpg = models.BooleanField("lpg", default=False)
    reefer = models.BooleanField("reefer", default=False)
    ro_ro = models.BooleanField("ro_ro", default=False)
    heavy_lift = models.BooleanField("heavy_lift", default=False)
    passenger = models.BooleanField("passenger", default=False)
    off_shore = models.BooleanField("off_shore", default=False)
    ferry = models.BooleanField("ferry", default=False)
    tug = models.BooleanField("tug", default=False)
    
    def __str__(self):
        return self.name
        
class UserSelectedCompany(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    selected_companies = models.ManyToManyField('cvsender.Company', related_name='selected_companies')
    send_from_email = models.EmailField("send_from_email", max_length = 200, null=True)
    cv = models.CharField("cv", max_length=255, null=True)
    text = models.CharField("text", max_length=255, null=True)
    
    def __str__(self):
        return self.user