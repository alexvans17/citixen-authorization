# Generated by Django 3.0 on 2019-12-16 17:43

import corexen.utils.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120, unique=True)),
                ('national_flag', models.ImageField(upload_to=corexen.utils.models.RandomFileName('country/images/'))),
            ],
            options={
                'ordering': ('-created_at', '-updated_at'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LanguageCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120, unique=True)),
                ('code', models.CharField(max_length=120, unique=True)),
            ],
            options={
                'ordering': ('-created_at', '-updated_at'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LatLngBounds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('northeast_latitude', models.DecimalField(decimal_places=15, default=0, max_digits=18)),
                ('northeast_longitude', models.DecimalField(decimal_places=15, default=0, max_digits=18)),
                ('southwest_latitude', models.DecimalField(decimal_places=15, default=0, max_digits=18)),
                ('southwest_longitude', models.DecimalField(decimal_places=15, default=0, max_digits=18)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120, unique=True)),
                ('flag', models.ImageField(upload_to=corexen.utils.models.RandomFileName('city/images/'))),
                ('google_map_key', models.CharField(max_length=150)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='internationalization.Country')),
                ('map_bounds', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='internationalization.LatLngBounds')),
            ],
            options={
                'ordering': ('-created_at', '-updated_at'),
                'abstract': False,
            },
        ),
    ]
