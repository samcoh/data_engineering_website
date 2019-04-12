# Generated by Django 2.1.5 on 2019-04-12 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people_major',
            name='major',
        ),
        migrations.RemoveField(
            model_name='people_major',
            name='people',
        ),
        migrations.RemoveField(
            model_name='people_minor',
            name='minor',
        ),
        migrations.RemoveField(
            model_name='people_minor',
            name='people',
        ),
        migrations.RemoveField(
            model_name='people_project',
            name='people',
        ),
        migrations.RemoveField(
            model_name='people_project',
            name='project',
        ),
        migrations.AlterField(
            model_name='major',
            name='peoples',
            field=models.ManyToManyField(blank=True, default='None', to='catalog.People'),
        ),
        migrations.AlterField(
            model_name='minor',
            name='peoples',
            field=models.ManyToManyField(blank=True, default='None', to='catalog.People'),
        ),
        migrations.AlterField(
            model_name='people',
            name='majors',
            field=models.ManyToManyField(blank=True, default='Undeclared', help_text="Select your major(s).(Hold down 'Control', or 'Command' on a Mac, to select more than one)", to='catalog.Major', verbose_name='Major(s)'),
        ),
        migrations.AlterField(
            model_name='people',
            name='minors',
            field=models.ManyToManyField(blank=True, help_text="Select your minor(s).(Hold down 'Control', or 'Command' on a Mac, to select more than one)", to='catalog.Minor', verbose_name='Minor(s)'),
        ),
        migrations.AlterField(
            model_name='people',
            name='projects',
            field=models.ManyToManyField(blank=True, help_text="Select all Projects you have worked on.(Hold down 'Control', or 'Command' on a Mac, to select more than one)", to='catalog.Project', verbose_name='Project(s)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='peoples',
            field=models.ManyToManyField(blank=True, default='None', help_text="Select all individuals who contributed to the project. (Hold down 'Control', or 'Command' on a Mac, to select more than one)", to='catalog.People', verbose_name='contributors'),
        ),
        migrations.DeleteModel(
            name='People_Major',
        ),
        migrations.DeleteModel(
            name='People_Minor',
        ),
        migrations.DeleteModel(
            name='People_Project',
        ),
    ]
