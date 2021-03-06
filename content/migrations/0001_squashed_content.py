# Generated by Django 4.0.4 on 2022-05-26 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('content', '0001_initial'), ('content', '0002_comment'), ('content', '0003_rename_content_post_text'), ('content', '0004_alter_post_options_delete_comment'), ('content', '0005_alter_post_options_comment'), ('content', '0006_alter_comment_options_alter_post_options'), ('content', '0007_post2'), ('content', '0008_rename_post_tweet_delete_post2'), ('content', '0009_tweet_users_like'), ('content', '0010_tweet_hits'), ('content', '0011_alter_tweet_options_alter_tweet_date_edit'), ('content', '0012_alter_tweet_options'), ('content', '0013_action'), ('content', '0014_action_date'), ('content', '0015_alter_action_content_type_alter_action_object_id'), ('content', '0016_alter_action_options_alter_tweet_id'), ('content', '0017_alter_tweet_id'), ('content', '0018_rename_tweet_post')]

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('title', models.CharField(max_length=30)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_edit', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('users_like', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('hits', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('-date_create',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_edit', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='content.post')),
            ],
            options={
                'ordering': ('-date_create',),
            },
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb', models.CharField(max_length=30)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action', to=settings.AUTH_USER_MODEL)),
                ('date', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
