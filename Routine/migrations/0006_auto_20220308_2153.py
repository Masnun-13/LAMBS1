# Generated by Django 3.1.7 on 2022-03-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Routine', '0005_auto_20210410_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitylist',
            name='alist_priority',
            field=models.IntegerField(db_column='Activity Priority', default=0, verbose_name='Activity Priority'),
        ),
        migrations.AddField(
            model_name='activitylist',
            name='alist_stime',
            field=models.IntegerField(db_column='Starting time', default=0, verbose_name='Starting time'),
        ),
        migrations.AlterField(
            model_name='activitylist',
            name='alist_day',
            field=models.CharField(db_column='Day', default='Sunday', max_length=10, verbose_name='Day of Week'),
        ),
        migrations.AlterField(
            model_name='routine',
            name='routine_day',
            field=models.CharField(db_column='Day', default='Sunday', max_length=10, verbose_name='Day of Week'),
        ),
    ]
