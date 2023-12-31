# Generated by Django 4.2 on 2023-06-23 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import words.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('translate', models.CharField(max_length=200)),
                ('transcription', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, upload_to=words.models.image_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('words', models.ManyToManyField(to='words.word')),
            ],
        ),
    ]
