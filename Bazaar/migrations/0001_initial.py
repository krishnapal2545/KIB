# Generated by Django 3.1.7 on 2021-05-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beauty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('descrip', models.CharField(max_length=5000)),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Electronics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('descrip', models.CharField(max_length=5000)),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Fashion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('descrip', models.CharField(max_length=5000)),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('descrip', models.CharField(max_length=5000)),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('descrip', models.CharField(max_length=5000)),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('descrip', models.CharField(max_length=5000)),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('descrip', models.CharField(max_length=5000)),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
