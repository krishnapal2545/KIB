# Generated by Django 3.1.7 on 2021-05-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secretkey', models.CharField(max_length=200)),
                ('debug', models.BooleanField(default=True)),
                ('host_user', models.EmailField(max_length=254)),
                ('host_password', models.CharField(max_length=200)),
                ('account_sid', models.CharField(max_length=500)),
                ('account_token', models.CharField(max_length=500)),
                ('phonenumber', models.CharField(max_length=100)),
            ],
        ),
    ]
