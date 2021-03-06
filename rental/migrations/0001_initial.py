# Generated by Django 3.0.14 on 2022-05-31 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=15)),
                ('propertyphotos', models.ImageField(upload_to='property/')),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('status', models.CharField(max_length=30)),
                ('rooms', models.FloatField()),
                ('period', models.CharField(max_length=15)),
            ],
        ),
    ]
