# Generated by Django 2.1.5 on 2019-03-25 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20190322_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='section_id',
            field=models.ForeignKey(default='None', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Section'),
        ),
    ]
