# Generated by Django 5.0.3 on 2024-04-13 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_remove_bookrent_lending_time_alter_bookrent_book'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookrent',
            options={'managed': False},
        ),
    ]
