# Generated by Django 3.0.2 on 2020-02-24 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0007_auto_20200224_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='UE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=40)),
                ('codeUE', models.CharField(max_length=40)),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentification.Departement')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=40)),
                ('CM', models.IntegerField()),
                ('TD_TP', models.IntegerField()),
                ('TPE', models.IntegerField()),
                ('ECTS', models.IntegerField()),
                ('coef', models.IntegerField()),
                ('UE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentification.UE')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentification.Classe')),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=40)),
                ('semestre', models.IntegerField()),
                ('coef', models.IntegerField()),
                ('charge_horaire', models.IntegerField()),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentification.Classe')),
            ],
        ),
    ]
