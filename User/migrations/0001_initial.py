# Generated by Django 3.1.7 on 2021-04-02 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_firstname', models.CharField(db_column='First name', default='John', max_length=20)),
                ('user_lastname', models.CharField(db_column='Last name', default='Doe', max_length=20)),
                ('user_age', models.IntegerField(db_column='Age', default=0)),
                ('user_occupation', models.CharField(db_column='Occupation', default='None', max_length=50)),
            ],
            options={
                'db_table': 'User Info',
            },
        ),
    ]
