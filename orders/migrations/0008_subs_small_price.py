# Generated by Django 2.1.5 on 2020-05-04 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200504_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='subs_small',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
