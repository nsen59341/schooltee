# Generated by Django 5.1.4 on 2024-12-20 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=96)),
                ('topic', models.CharField(default='General', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=96)),
                ('email', models.EmailField(max_length=124)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teeapp.lesson')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teeapp.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=96)),
                ('email', models.EmailField(max_length=124)),
                ('assignment', models.ManyToManyField(to='teeapp.assignment')),
                ('lesson', models.ManyToManyField(to='teeapp.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Permormance',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('marks', models.FloatField(max_length=64)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teeapp.assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teeapp.student')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teeapp.teacher'),
        ),
    ]
