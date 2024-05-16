# Generated by Django 5.0.6 on 2024-05-16 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dir', models.CharField(max_length=255)),
                ('basename', models.CharField(max_length=255)),
                ('refname', models.CharField(max_length=255)),
                ('ekstension', models.CharField(max_length=10)),
                ('filesize', models.BigIntegerField()),
                ('added_to_geoserver', models.BooleanField(default=False)),
                ('url_geoserver', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(upload_to='backend/fews/repository'),
        ),
    ]
