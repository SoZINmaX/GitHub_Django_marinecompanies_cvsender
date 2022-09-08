# Generated by Django 4.0.6 on 2022-09-02 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvsender', '0007_alter_userselectedcompany_cv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='cadet',
        ),
        migrations.RemoveField(
            model_name='company',
            name='chemical_tanker',
        ),
        migrations.RemoveField(
            model_name='company',
            name='link',
        ),
        migrations.RemoveField(
            model_name='company',
            name='lng',
        ),
        migrations.RemoveField(
            model_name='company',
            name='lpg',
        ),
        migrations.RemoveField(
            model_name='company',
            name='product_tanker',
        ),
        migrations.AddField(
            model_name='company',
            name='adress',
            field=models.CharField(max_length=200, null=True, verbose_name='adress'),
        ),
        migrations.AddField(
            model_name='company',
            name='cadet_program',
            field=models.BooleanField(default=False, verbose_name='cadet_program'),
        ),
        migrations.AddField(
            model_name='company',
            name='fishing',
            field=models.BooleanField(default=False, verbose_name='fishing'),
        ),
        migrations.AddField(
            model_name='company',
            name='phone_number',
            field=models.CharField(max_length=200, null=True, verbose_name='phone_number'),
        ),
        migrations.AddField(
            model_name='company',
            name='website_info',
            field=models.URLField(null=True, verbose_name='website_info'),
        ),
        migrations.AddField(
            model_name='company',
            name='yachts',
            field=models.BooleanField(default=False, verbose_name='yachts'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='name'),
        ),
    ]