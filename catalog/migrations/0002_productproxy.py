# Generated by Django 2.1 on 2018-11-28 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Relatorio',
                'verbose_name_plural': 'Relatorios',
                'proxy': True,
                'indexes': [],
            },
            bases=('catalog.product',),
        ),
    ]
