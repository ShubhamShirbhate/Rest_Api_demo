# Generated by Django 2.1.5 on 2020-10-16 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('withoutLink', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
