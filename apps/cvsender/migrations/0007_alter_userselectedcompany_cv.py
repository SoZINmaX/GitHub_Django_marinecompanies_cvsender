# Generated by Django 4.0.6 on 2022-08-18 23:43

import apps.cvsender.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvsender', '0006_alter_userselectedcompany_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userselectedcompany',
            name='cv',
            field=models.FileField(null=True, upload_to=apps.cvsender.models.UserSelectedCompany.user_directory_path, verbose_name='cv'),
        ),
    ]