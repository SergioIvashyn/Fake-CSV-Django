# Generated by Django 2.2.6 on 2021-01-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210121_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schemacolumn',
            name='range_max',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='schemacolumn',
            name='range_min',
            field=models.IntegerField(default=0),
        ),
    ]
