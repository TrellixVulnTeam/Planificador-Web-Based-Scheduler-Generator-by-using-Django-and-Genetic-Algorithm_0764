# Generated by Django 4.0.3 on 2022-07-05 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttgen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studnts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.CharField(max_length=13)),
                ('s_name', models.CharField(max_length=25)),
            ],
        ),
    ]