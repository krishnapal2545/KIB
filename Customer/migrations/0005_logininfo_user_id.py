# Generated by Django 3.1.7 on 2021-05-26 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0004_logininfo_is_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='logininfo',
            name='User_ID',
            field=models.PositiveIntegerField(default=0),
        ),
    ]