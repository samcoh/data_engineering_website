# Generated by Django 2.1.5 on 2019-02-03 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20190203_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='end_month',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='start_month',
            new_name='start_date',
        ),
        migrations.AlterField(
            model_name='people',
            name='role',
            field=models.CharField(choices=[('MEM', 'Member'), ('SRE', 'Senior Editor')], default='MEM', max_length=3),
        ),
    ]
