# Generated by Django 5.1.4 on 2024-12-24 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teeapp', '0004_alter_permormance_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='assignment',
            field=models.ManyToManyField(null=True, to='teeapp.assignment'),
        ),
        migrations.AlterField(
            model_name='student',
            name='lesson',
            field=models.ManyToManyField(null=True, to='teeapp.lesson'),
        ),
    ]
