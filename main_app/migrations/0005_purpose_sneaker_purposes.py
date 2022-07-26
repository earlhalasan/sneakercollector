# Generated by Django 4.0.4 on 2022-07-20 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_release_options_alter_release_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='sneaker',
            name='purposes',
            field=models.ManyToManyField(to='main_app.purpose'),
        ),
    ]
