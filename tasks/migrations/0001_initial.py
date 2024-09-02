# Generated by Django 5.1 on 2024-09-01 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Prioridade',
                'verbose_name_plural': 'Prioridades',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, unique=True)),
                ('description', models.CharField(max_length=250)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tasks.category')),
                ('participants', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.group')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tasks.priority')),
            ],
            options={
                'verbose_name': 'Tarefa',
                'verbose_name_plural': 'Tarefas',
            },
        ),
    ]
