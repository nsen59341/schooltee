# Generated by Django 5.1.4 on 2024-12-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teeapp', '0003_remove_permormance_marks_permormance_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permormance',
            name='percentage',
            field=models.IntegerField(),
        ),
    ]
