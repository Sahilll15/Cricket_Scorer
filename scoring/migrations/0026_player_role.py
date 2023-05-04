# Generated by Django 4.1.7 on 2023-05-03 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0025_alter_makematch_tournament_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='role',
            field=models.CharField(choices=[('Batsman', 'Batsman'), ('Bowler', 'Bowler')], default='Batsman', max_length=7),
        ),
    ]