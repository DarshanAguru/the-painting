# Generated by Django 4.2 on 2023-04-15 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_users_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scoreandtime',
            name='cl0Scr',
        ),
        migrations.RemoveField(
            model_name='scoreandtime',
            name='cl0Tym',
        ),
        migrations.RemoveField(
            model_name='scoreandtime',
            name='cl9Scr',
        ),
        migrations.RemoveField(
            model_name='scoreandtime',
            name='cl9Tym',
        ),
    ]
