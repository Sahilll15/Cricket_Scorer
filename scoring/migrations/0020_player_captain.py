# Generated by Django 4.1.7 on 2023-03-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0019_remove_team_captian_email_remove_team_captian_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='captain',
            field=models.BooleanField(default=False),
        ),
    ]
