# Generated by Django 2.2.1 on 2019-05-19 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190517_1605'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-id']},
        ),
    ]
