# Generated by Django 3.2.3 on 2023-08-23 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]