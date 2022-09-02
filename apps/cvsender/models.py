from django.db import models
from apps.authentication.models import User

class Company(models.Model):
    
    name = models.CharField("name", max_length=200, null=True)
    adress = models.CharField("adress", max_length=200, null=True)
    website_info = models.URLField("website_info", max_length=200, null=True)
    email = models.EmailField("email", max_length = 200, null=True)
    phone_number = models.CharField("phone_number", max_length=200, null=True)
    cadet_program = models.BooleanField("cadet_program", default=False)
    container = models.BooleanField("container", default=False)
    bulk = models.BooleanField("bulk", default=False)
    tanker = models.BooleanField("tanker", default=False)
    gas_carrier = models.BooleanField("gas_carrier", default=False)
    reefer = models.BooleanField("reefer", default=False)
    ro_ro = models.BooleanField("ro_ro", default=False)
    heavy_lift = models.BooleanField("heavy_lift", default=False)
    passenger = models.BooleanField("passenger", default=False)
    off_shore = models.BooleanField("off_shore", default=False)
    yachts = models.BooleanField("yachts", default=False)
    fishing = models.BooleanField("fishing", default=False)
    tug = models.BooleanField("tug", default=False)
    ferry = models.BooleanField("ferry", default=False)
    
    def __str__(self):
        return self.name
        
class UserSelectedCompany(models.Model):

    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.user.id, filename)
    
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    selected_companies = models.ManyToManyField('cvsender.Company', related_name='selected_companies')
    send_from_email = models.EmailField("send_from_email", max_length = 200, null=True)
    cv = models.FileField("cv", upload_to=user_directory_path, null = True)
    text = models.CharField("text", max_length=255, null=True)
    
    def __str__(self):
        return self.user