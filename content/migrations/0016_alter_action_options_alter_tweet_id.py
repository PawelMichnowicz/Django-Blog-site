# Generated by Django 4.0.4 on 2022-05-11 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_alter_action_content_type_alter_action_object_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='action',
            options={'ordering': ('-date',)},
        ),
        migrations.AlterField(
            model_name='tweet',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
