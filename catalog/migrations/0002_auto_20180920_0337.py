# Generated by Django 2.1 on 2018-09-20 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='size',
            options={'ordering': ['size'], 'verbose_name': 'Tamanho', 'verbose_name_plural': 'Tamanhos'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='sizes',
            new_name='size',
        ),
    ]
