# Generated by Django 2.2.4 on 2019-10-02 19:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('nit', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=100)),
                ('country', models.CharField(max_length=60)),
                ('image_url', models.ImageField(upload_to='companies/images/')),
                ('is_active', models.BooleanField(default=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Headquarter',
            fields=[
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=120)),
                ('image_url', models.ImageField(upload_to='headquarters/images/')),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=120)),
                ('neighborhood', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=60)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('recruitment', models.BooleanField(default=False)),
                ('recruitment_message', models.CharField(blank=True, max_length=250, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
            ],
        ),
    ]
