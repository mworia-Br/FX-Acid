# Generated by Django 4.2.5 on 2023-09-24 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_wallet_transaction_systemdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='system',
            old_name='short_description',
            new_name='trading_style',
        ),
    ]