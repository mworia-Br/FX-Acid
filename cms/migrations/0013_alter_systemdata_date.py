# Generated by Django 4.2.5 on 2023-10-05 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_systemdata_date_systemdata_roi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemdata',
            name='date',
            field=models.DateField(null=True),
        ),
    ]