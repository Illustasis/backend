# Generated by Django 4.0.4 on 2022-05-26 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0002_article_book_collect_reply_score_user_delete_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='introduction',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
