# Generated by Django 2.2.10 on 2020-03-28 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200315_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='professional',
            name='last_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]