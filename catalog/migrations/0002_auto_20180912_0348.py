# Generated by Django 2.1 on 2018-09-12 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='create',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='create',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]