# Generated by Django 3.0.6 on 2020-05-20 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20200519_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='quote',
            field=models.CharField(default='-', max_length=255),
            preserve_default=False,
        ),
    ]
