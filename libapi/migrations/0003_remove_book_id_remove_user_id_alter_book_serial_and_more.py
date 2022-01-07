# Generated by Django 4.0.1 on 2022-01-07 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapi', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='book',
            name='serial',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='regNo',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
