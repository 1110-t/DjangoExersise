# Generated by Django 3.2.18 on 2023-04-07 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('birthday', models.DateTimeField()),
                ('gender', models.CharField(max_length=1)),
                ('bloodtype', models.CharField(max_length=1)),
                ('profile', models.CharField(max_length=100)),
            ],
        ),
    ]
