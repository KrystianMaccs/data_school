# Generated by Django 3.2.7 on 2022-03-30 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default=True, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curriculum',
            name='name',
            field=models.CharField(default=True, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='name',
            field=models.CharField(default=True, max_length=120),
            preserve_default=False,
        ),
    ]
