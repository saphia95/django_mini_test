# Generated by Django 3.0.7 on 2020-06-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20200622_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='name',
            field=models.CharField(default='test', max_length=200),
        ),
    ]