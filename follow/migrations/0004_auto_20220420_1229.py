# Generated by Django 3.1 on 2022-04-20 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0003_auto_20220420_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
