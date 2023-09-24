# Generated by Django 4.2.5 on 2023-09-24 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CopyTrader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(blank=True, max_length=255, null=True, verbose_name='Unique order ID')),
                ('ordered_date', models.DateTimeField(auto_now_add=True, verbose_name='Ordered Date')),
                ('status', models.CharField(choices=[('Not Paid', 'Not Paid'), ('Paid', 'Paid'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Not Paid', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.systems', verbose_name='System'),
        ),
        migrations.RenameModel(
            old_name='Systems',
            new_name='System',
        ),
        migrations.DeleteModel(
            name='CopyTraders',
        ),
        migrations.AddField(
            model_name='copytrader',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.system', verbose_name='System'),
        ),
        migrations.AddField(
            model_name='copytrader',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
