# Generated by Django 2.2.4 on 2019-08-25 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190825_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestprofile',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hostprofile',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
            preserve_default=False,
        ),
    ]
