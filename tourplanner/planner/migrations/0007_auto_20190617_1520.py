# Generated by Django 2.2.1 on 2019-06-17 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0006_auto_20190617_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Email',
            field=models.EmailField(max_length=50),
        ),
    ]
