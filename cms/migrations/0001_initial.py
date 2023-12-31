# Generated by Django 4.2.5 on 2023-09-24 02:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Systems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('short_description', models.CharField(blank=True, max_length=100, null=True)),
                ('pricing', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('roi', models.CharField(blank=True, max_length=50, null=True)),
                ('LastProfit', models.CharField(blank=True, max_length=50, null=True)),
                ('LastProfitWinRate', models.CharField(blank=True, max_length=50, null=True)),
                ('TotalProfits', models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True)),
                ('TotalCopyTraders', models.CharField(blank=True, max_length=50, null=True)),
                ('AUM', models.CharField(blank=True, max_length=50, null=True)),
                ('telegram', models.CharField(blank=True, max_length=200, null=True)),
                ('telegram_visible', models.BooleanField(default=False)),
                ('discord', models.CharField(blank=True, max_length=200, null=True)),
                ('discord_visible', models.BooleanField(default=False)),
                ('youtube', models.CharField(blank=True, max_length=200, null=True)),
                ('youtube_visible', models.BooleanField(default=False)),
                ('full', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CopyTraders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(blank=True, max_length=255, null=True, verbose_name='Unique order ID')),
                ('ordered_date', models.DateTimeField(auto_now_add=True, verbose_name='Ordered Date')),
                ('status', models.CharField(choices=[('Not Paid', 'Not Paid'), ('Paid', 'Paid'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Not Paid', max_length=50)),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.systems', verbose_name='Systems')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.systems', verbose_name='Systems')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
