# Generated by Django 4.0.6 on 2022-10-25 07:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribedUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date created')),
            ],
        ),
    ]
