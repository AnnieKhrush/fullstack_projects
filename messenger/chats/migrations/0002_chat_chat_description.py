# Generated by Django 4.1.2 on 2022-10-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='chat_description',
            field=models.TextField(null=True),
        ),
    ]
