# Generated by Django 2.1.5 on 2019-03-22 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20190322_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(blank=True, default='nothing', help_text='Section', max_length=50, null=True),
        ),
    ]