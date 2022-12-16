# Generated by Django 4.1.4 on 2022-12-15 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auth_datas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('asker_login', models.CharField(max_length=30)),
                ('controler_login', models.CharField(max_length=30)),
                ('controler_auth', models.CharField(choices=[('AUTHORIZED', 'Authorized'), ('REFUSED', 'Refused'), ('PENDING', 'Pending')], default='PENDING', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Auth_users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=5, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
