# Generated by Django 3.0.2 on 2020-02-29 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0013_auto_20200229_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casemodule',
            name='jour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentification.Jour'),
        ),
    ]
