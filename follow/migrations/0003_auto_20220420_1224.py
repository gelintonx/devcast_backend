# Generated by Django 3.1 on 2022-04-20 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0002_auto_20220420_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
