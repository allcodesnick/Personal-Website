# Generated by Django 3.1.2 on 2020-11-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0003_auto_20201112_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_application',
            name='company_website',
            field=models.URLField(max_length=100),
        ),
    ]
