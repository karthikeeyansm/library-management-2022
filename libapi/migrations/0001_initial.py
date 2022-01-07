# Generated by Django 4.0.1 on 2022-01-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField()),
                ('Name', models.CharField(max_length=60)),
                ('author', models.CharField(max_length=50)),
                ('date_of_pub', models.DateField()),
                ('description', models.CharField(max_length=250)),
                ('no_of_borrowed', models.IntegerField()),
                ('bookStock', models.IntegerField()),
            ],
        ),
    ]
