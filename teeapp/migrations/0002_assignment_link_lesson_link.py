# Generated by Django 5.1.4 on 2024-12-20 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='link',
            field=models.URLField(default='Dummy', max_length=1050),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='link',
            field=models.URLField(default='Dummy', max_length=1050),
            preserve_default=False,
        ),
    ]
