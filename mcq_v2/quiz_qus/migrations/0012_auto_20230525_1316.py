# Generated by Django 3.0 on 2023-05-25 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_qus', '0011_auto_20230525_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subquestion',
            name='ans',
            field=models.TextField(null=True),
        ),
    ]
