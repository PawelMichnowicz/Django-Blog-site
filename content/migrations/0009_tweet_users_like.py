# Generated by Django 4.0.4 on 2022-04-30 13:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0008_rename_post_tweet_delete_post2'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
