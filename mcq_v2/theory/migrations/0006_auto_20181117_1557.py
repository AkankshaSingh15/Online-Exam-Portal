# Generated by Django 2.1.2 on 2018-11-17 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theory', '0005_auto_20181117_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quest',
            name='desc1',
        ),
        migrations.RemoveField(
            model_name='quest',
            name='desc2',
        ),
        migrations.RemoveField(
            model_name='quest',
            name='desc3',
        ),
        migrations.RemoveField(
            model_name='quest',
            name='desc4',
        ),
        migrations.RemoveField(
            model_name='quest',
            name='desc5',
        ),
        migrations.RemoveField(
            model_name='quest',
            name='desc6',
        ),
        migrations.AddField(
            model_name='quest',
            name='desc',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]