# Generated by Django 2.2 on 2020-05-15 12:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0007_auto_20200515_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image_path', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('alt_text', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]