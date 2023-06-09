# Generated by Django 4.1.7 on 2023-04-13 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0021_alter_batter_balls_faced_alter_batter_fours_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='makematch',
            old_name='team_1',
            new_name='team_a_name',
        ),
        migrations.RenameField(
            model_name='makematch',
            old_name='team_2',
            new_name='team_b_name',
        ),
        migrations.AddField(
            model_name='makematch',
            name='team_a_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='makematch',
            name='team_b_score',
            field=models.IntegerField(default=0),
        ),
    ]
