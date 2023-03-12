# Generated by Django 4.1.7 on 2023-03-12 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0002_remove_tournament_matchpin_remove_tournament_team1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='tournament',
        ),
        migrations.AddField(
            model_name='team',
            name='captain_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='team',
            name='contact_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='teams',
            field=models.ManyToManyField(blank=True, related_name='tournaments', to='scoring.team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Match',
        ),
    ]