# Generated by Django 2.1.2 on 2021-06-05 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Registration_num', models.CharField(max_length=7)),
                ('Roll_num', models.IntegerField()),
                ('Hostel', models.CharField(max_length=30)),
                ('Room_number', models.CharField(max_length=6)),
                ('Phone_num', models.CharField(max_length=15)),
                ('Course', models.CharField(max_length=8)),
                ('Photo', models.ImageField(upload_to='upload_images')),
            ],
        ),
    ]
