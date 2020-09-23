# Generated by Django 3.1.1 on 2020-09-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MelonList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('singer', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
            ],
        ),
    ]
