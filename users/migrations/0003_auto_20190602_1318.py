# Generated by Django 2.2.1 on 2019-06-02 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'ECellUser', 'verbose_name_plural': 'ECellUsers'},
        ),
    ]
