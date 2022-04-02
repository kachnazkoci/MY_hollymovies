# Generated by Django 3.2.12 on 2022-04-02 08:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='released',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]