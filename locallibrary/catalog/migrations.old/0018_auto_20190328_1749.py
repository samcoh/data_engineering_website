# Generated by Django 2.1.5 on 2019-03-28 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_auto_20190327_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(help_text='Project Name', max_length=400),
        ),
    ]
