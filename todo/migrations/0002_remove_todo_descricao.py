# Generated by Django 4.1 on 2022-08-28 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='Descricao',
        ),
    ]