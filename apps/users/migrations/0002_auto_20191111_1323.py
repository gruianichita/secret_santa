# Generated by Django 2.2.7 on 2019-11-11 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='invited',
        ),
        migrations.RemoveField(
            model_name='user',
            name='registration_code',
        ),
    ]
