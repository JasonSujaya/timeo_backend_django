# Generated by Django 2.2 on 2020-05-15 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0006_auto_20200515_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='notification_newsletter',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='notifictioon_post',
            field=models.BooleanField(default=True),
        ),
    ]