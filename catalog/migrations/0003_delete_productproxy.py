# Generated by Django 2.1 on 2018-11-28 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_productproxy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductProxy',
        ),
    ]