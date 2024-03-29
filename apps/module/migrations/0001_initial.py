# Generated by Django 4.1 on 2023-04-02 12:46

from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=6, max_length=6, prefix='', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('course_id', models.UUIDField()),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='thumbnails/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=6, max_length=6, prefix='', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TagModule',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=6, max_length=6, prefix='', primary_key=True, serialize=False)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module.module')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module.tag')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='tags',
            field=models.ManyToManyField(through='module.TagModule', to='module.tag'),
        ),
        migrations.AddIndex(
            model_name='module',
            index=models.Index(fields=['course_id'], name='module_serv_course__0f5b85_idx'),
        ),
        migrations.AddIndex(
            model_name='module',
            index=models.Index(fields=['created_at'], name='module_serv_created_b44fa3_idx'),
        ),
    ]
