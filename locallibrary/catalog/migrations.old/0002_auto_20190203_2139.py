# Generated by Django 2.1.5 on 2019-02-03 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={'ordering': ['last_name', 'first_name'], 'verbose_name': 'People'},
        ),
    ]
