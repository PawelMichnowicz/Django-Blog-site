# Generated by Django 4.0.4 on 2022-05-05 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_alter_tweet_options_alter_tweet_date_edit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ('-date_create',)},
        ),
    ]
