# Generated by Django 2.2.4 on 2019-08-18 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guestprofile',
            options={'default_related_name': 'guest', 'verbose_name': 'Guest', 'verbose_name_plural': 'Guests'},
        ),
        migrations.AlterModelOptions(
            name='hostprofile',
            options={'default_related_name': 'host', 'verbose_name': 'Host', 'verbose_name_plural': 'Hosts'},
        ),
    ]
