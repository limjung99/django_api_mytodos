# Generated by Django 4.2 on 2023-05-08 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('user_pw', models.CharField(max_length=200)),
                ('user_email', models.CharField(max_length=100)),
            ],
        ),
    ]
