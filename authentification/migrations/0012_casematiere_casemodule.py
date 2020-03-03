# Generated by Django 3.0.2 on 2020-02-28 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0011_auto_20200225_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.CharField(max_length=40)),
                ('heure_debut', models.IntegerField()),
                ('heure_fin', models.IntegerField()),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentification.Module')),
            ],
        ),
        migrations.CreateModel(
            name='CaseMatiere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.CharField(max_length=40)),
                ('heure_debut', models.IntegerField()),
                ('heure_fin', models.IntegerField()),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentification.Matiere')),
            ],
        ),
    ]
