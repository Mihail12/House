# Generated by Django 2.0.7 on 2018-07-19 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_house_housemates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housemates',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
