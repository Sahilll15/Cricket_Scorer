# Generated by Django 4.1.7 on 2023-03-14 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0005_makematch'),
    ]

    operations = [
        migrations.AddField(
            model_name='makematch',
            name='match_pin',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
