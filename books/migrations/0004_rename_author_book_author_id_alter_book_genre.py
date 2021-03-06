# Generated by Django 4.0.3 on 2022-04-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='author_id',
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('horror', 'horror'), ('drama', 'drama'), ('self_development', 'self_development'), ('scifi', 'scifi')], max_length=256),
        ),
    ]
