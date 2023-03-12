# Generated by Django 4.1.7 on 2023-03-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0003_remove_team_tournament_team_captain_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='captain_name',
        ),
        migrations.RemoveField(
            model_name='team',
            name='contact_number',
        ),
        migrations.RemoveField(
            model_name='team',
            name='email',
        ),
        migrations.AddField(
            model_name='team',
            name='captian_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='captian_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='captian_phone',
            field=models.IntegerField(null=True),
        ),
    ]
