# Generated by Django 3.0.5 on 2020-06-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('princ', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='normalprod',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]
