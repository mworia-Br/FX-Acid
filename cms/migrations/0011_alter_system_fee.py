# Generated by Django 4.2.5 on 2023-10-04 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_remove_system_pricing_system_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='fee',
            field=models.PositiveIntegerField(default=500),
        ),
    ]
