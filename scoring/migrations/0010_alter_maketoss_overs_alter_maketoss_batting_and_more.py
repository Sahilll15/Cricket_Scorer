# Generated by Django 4.1.7 on 2023-03-14 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0009_alter_makematch_team_2_alter_maketoss_batting_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maketoss',
            name='Overs',
            field=models.IntegerField(default=5, null=True),
        ),
        migrations.AlterField(
            model_name='maketoss',
            name='batting',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='maketoss',
            name='toss',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
