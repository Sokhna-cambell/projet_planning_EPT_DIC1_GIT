# Generated by Django 3.0.2 on 2020-02-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0010_ue_nbre_modules'),
    ]

    operations = [
        migrations.AddField(
            model_name='departement',
            name='systeme',
            field=models.CharField(default='semestriel', max_length=30, verbose_name='nom_dept'),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='profil',
            field=models.ImageField(default='/media/photos/avatar1.png/', upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='profil',
            field=models.ImageField(default='/media/photos/avatar1.png/', upload_to='photos/'),
        ),
    ]
