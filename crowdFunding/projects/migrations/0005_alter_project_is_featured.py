# Generated by Django 4.1.1 on 2022-09-21 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20220917_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='is_featured',
            field=models.BooleanField(default=True),
        ),
    ]
