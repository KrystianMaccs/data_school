# Generated by Django 3.2.7 on 2022-03-19 13:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membership', '0003_auto_20220319_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('allowed_membership', models.ManyToManyField(to='membership.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=120)),
                ('position', models.IntegerField()),
                ('video_url', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]