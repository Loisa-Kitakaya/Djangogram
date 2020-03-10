# Generated by Django 3.0.3 on 2020-03-10 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('image_name', models.CharField(max_length=30)),
                ('image_caption', models.CharField(max_length=200)),
                ('image_comments', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='media/')),
                ('profile_bio', models.CharField(max_length=400)),
            ],
        ),
    ]