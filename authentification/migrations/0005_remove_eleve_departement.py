# Generated by Django 3.0.2 on 2020-02-21 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0004_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleve',
            name='departement',
        ),
    ]