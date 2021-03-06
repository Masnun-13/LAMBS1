# Generated by Django 3.1.7 on 2021-03-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routine_user', models.CharField(db_column='User', max_length=20)),
                ('routine_time', models.IntegerField(db_column='Time')),
                ('routine_activity', models.CharField(db_column='Activity', max_length=50)),
            ],
            options={
                'db_table': 'Routine',
            },
        ),
    ]
