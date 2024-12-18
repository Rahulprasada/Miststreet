# Generated by Django 5.1.3 on 2024-12-06 09:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_current_price_stockdetails_gain_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockdetails',
            old_name='Sold_Above',
            new_name='gain_percentage',
        ),
        migrations.RenameField(
            model_name='stockdetails',
            old_name='Gain',
            new_name='sold_above',
        ),
        migrations.RemoveField(
            model_name='stockdetails',
            name='Signal_Closed',
        ),
        migrations.RemoveField(
            model_name='stockdetails',
            name='Signal_Sent',
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='stock_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='stockdetails',
            name='signal_closed',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='stockdetails',
            name='signal_sent',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
