# Generated by Django 4.0.4 on 2022-06-07 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-likes', 'title']},
        ),
    ]
