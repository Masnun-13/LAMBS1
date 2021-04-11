# Generated by Django 3.1.7 on 2021-04-10 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Routine', '0004_auto_20210410_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitylist',
            name='alist_day',
            field=models.CharField(db_column='Day', default='Friday', max_length=10, verbose_name='Day of Week'),
        ),
        migrations.AddField(
            model_name='routine',
            name='routine_day',
            field=models.CharField(db_column='Day', default='Friday', max_length=10, verbose_name='Day of Week'),
        ),
        migrations.AlterField(
            model_name='activitylist',
            name='alist_activity',
            field=models.CharField(db_column='Activity', max_length=50, verbose_name='Activity'),
        ),
        migrations.AlterField(
            model_name='activitylist',
            name='alist_actno',
            field=models.IntegerField(db_column='Activity Number', default=0, verbose_name='Activity Number'),
        ),
        migrations.AlterField(
            model_name='activitylist',
            name='alist_time',
            field=models.IntegerField(db_column='Time Spent (Hours)', default=0, verbose_name='Time Spent (Hours)'),
        ),
        migrations.AlterField(
            model_name='activitylist',
            name='alist_username',
            field=models.CharField(db_column='User', max_length=20, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='routine',
            name='routine_activity',
            field=models.CharField(db_column='Activity', max_length=50, verbose_name='Activity'),
        ),
        migrations.AlterField(
            model_name='routine',
            name='routine_actno',
            field=models.IntegerField(db_column='Activity Number', default=0, verbose_name='Activity Number'),
        ),
        migrations.AlterField(
            model_name='routine',
            name='routine_time1',
            field=models.TimeField(db_column='Starting Time', verbose_name='Starting Time'),
        ),
        migrations.AlterField(
            model_name='routine',
            name='routine_time2',
            field=models.TimeField(db_column='Ending Time', verbose_name='Ending Time'),
        ),
        migrations.AlterField(
            model_name='routine',
            name='routine_user',
            field=models.CharField(db_column='User', max_length=20, verbose_name='User'),
        ),
    ]
