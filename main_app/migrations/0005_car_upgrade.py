# Generated by Django 4.1.7 on 2023-03-31 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_upgrade_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='upgrade',
            field=models.ManyToManyField(to='main_app.upgrade'),
        ),
    ]
