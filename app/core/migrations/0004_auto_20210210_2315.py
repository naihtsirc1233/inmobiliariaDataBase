# Generated by Django 3.1.6 on 2021-02-11 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210210_1144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persons',
            old_name='salary',
            new_name='salario',
        ),
        migrations.RemoveField(
            model_name='persons',
            name='age',
        ),
    ]