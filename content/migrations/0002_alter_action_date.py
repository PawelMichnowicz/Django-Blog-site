# Generated by Django 4.0.4 on 2022-05-30 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_squashed_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]