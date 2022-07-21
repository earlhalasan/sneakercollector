# Generated by Django 4.0.4 on 2022-07-20 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_sneaker_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.CharField(choices=[('O', 'Once'), ('T', 'Twice'), ('M', 'Multiple times')], default='O', max_length=1)),
                ('sneaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.sneaker')),
            ],
        ),
    ]
