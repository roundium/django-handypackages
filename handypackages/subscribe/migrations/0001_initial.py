# Generated by Django 2.2.1 on 2019-06-22 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Email')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Subscribe Time')),
            ],
            options={
                'verbose_name': 'Subscribe Email',
                'verbose_name_plural': 'Subscribe Emails',
                'abstract': False,
            },
        ),
    ]
