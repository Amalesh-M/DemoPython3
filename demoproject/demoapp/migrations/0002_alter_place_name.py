# Generated by Django 4.1.1 on 2022-09-29 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=350),
        ),
    ]
