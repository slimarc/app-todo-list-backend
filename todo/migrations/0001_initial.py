# Generated by Django 4.1 on 2022-08-26 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=250)),
                ('Descricao', models.TextField(blank=True)),
                ('Data', models.DateField()),
                ('Completado', models.BooleanField(default=False)),
            ],
        ),
    ]