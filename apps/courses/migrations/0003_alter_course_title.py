# Generated by Django 3.2.7 on 2022-03-29 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20220328_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.IntegerField(choices=[(1, 'Django Web Framework'), (2, 'Data Analysis'), (3, 'Data Science')]),
        ),
    ]