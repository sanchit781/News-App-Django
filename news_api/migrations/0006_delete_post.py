# Generated by Django 4.0.6 on 2022-10-25 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_api', '0005_alter_post_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]