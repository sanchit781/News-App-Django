# Generated by Django 4.0.6 on 2022-10-25 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_api', '0002_subscribedusers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribedusers',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='subscribedusers',
            name='name',
        ),
    ]
