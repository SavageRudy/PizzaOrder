# Generated by Django 2.1.5 on 2020-05-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20200505_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='large',
            name='id',
        ),
        migrations.AddField(
            model_name='large',
            name='large_id',
            field=models.IntegerField(default=100, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]