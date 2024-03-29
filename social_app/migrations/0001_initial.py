# Generated by Django 2.2.7 on 2019-11-05 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creating_profile_for', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('contactNo', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
                ('confirm', models.CharField(max_length=255)),
            ],
        ),
    ]
