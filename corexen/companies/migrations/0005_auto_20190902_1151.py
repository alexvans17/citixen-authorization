# Generated by Django 2.2.4 on 2019-09-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20190830_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='headquarter',
            name='country',
            field=models.CharField(max_length=60),
        ),
    ]
