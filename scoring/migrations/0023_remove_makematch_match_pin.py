# Generated by Django 4.1.7 on 2023-04-13 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0022_rename_team_1_makematch_team_a_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='makematch',
            name='match_pin',
        ),
    ]