# Generated by Django 4.1.3 on 2022-12-27 07:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('demo_link', models.CharField(blank=True, max_length=3000, null=True)),
                ('source_link', models.CharField(blank=True, max_length=3000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
