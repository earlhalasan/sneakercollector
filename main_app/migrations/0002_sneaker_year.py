# Generated by Django 4.0.4 on 2022-07-19 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneaker',
            name='year',
            field=models.IntegerField(default=2007),
            preserve_default=False,
        ),
    ]
