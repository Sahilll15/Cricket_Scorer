# Generated by Django 4.1.7 on 2023-03-13 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0004_remove_team_captain_name_remove_team_contact_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Makematch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_1', to='scoring.team')),
                ('team_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_2', to='scoring.team')),
                ('tournament_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoring.tournament')),
            ],
        ),
    ]
