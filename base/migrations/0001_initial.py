# Generated by Django 4.2 on 2023-04-13 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clueid', models.IntegerField()),
                ('clue', models.TextField()),
                ('score', models.IntegerField()),
                ('answer', models.TextField()),
            ],
        ),
    ]
