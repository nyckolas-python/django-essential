# Generated by Django 4.1.4 on 2023-08-23 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210329_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
