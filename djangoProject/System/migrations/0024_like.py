# Generated by Django 4.0.4 on 2022-06-05 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0023_user_isadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('resource_id', models.IntegerField(default=0)),
                ('column', models.IntegerField(default=0)),
            ],
        ),
    ]
