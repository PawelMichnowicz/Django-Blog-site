# Generated by Django 4.0.4 on 2022-04-26 16:40

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_remove_profile_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='def_avatar/davatar.png', upload_to=account.models.upload_location),
        ),
    ]
