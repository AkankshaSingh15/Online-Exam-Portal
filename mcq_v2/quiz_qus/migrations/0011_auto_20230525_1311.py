# Generated by Django 3.0 on 2023-05-25 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_qus', '0010_auto_20230525_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subquestion',
            name='correct_option',
            field=models.TextField(),
        ),
    ]