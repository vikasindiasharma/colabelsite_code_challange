# Generated by Django 2.2.6 on 2019-11-05 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=5000, unique=True)),
                ('image_label', models.CharField(max_length=9)),
                ('createdDate', models.DateTimeField(verbose_name='Created Date')),
            ],
        ),
        migrations.CreateModel(
            name='SampleImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=5000)),
            ],
        ),
    ]