# Generated by Django 3.2.9 on 2022-06-15 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0006_homeimgs'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='type',
            field=models.CharField(default='house', max_length=30),
            preserve_default=False,
        ),
    ]
