# Generated by Django 4.0.4 on 2022-04-29 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_alter_post_options_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-date_create',)},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-date_create',)},
        ),
    ]
