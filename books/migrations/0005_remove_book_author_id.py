# Generated by Django 4.0.3 on 2022-04-26 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_rename_author_book_author_id_alter_book_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author_id',
        ),
    ]