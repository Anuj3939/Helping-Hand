# Generated by Django 2.1.2 on 2021-06-10 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website_Home', '0003_foodplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit_place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=30)),
                ('Distance', models.CharField(max_length=7)),
                ('Mode', models.CharField(max_length=15)),
                ('Photo', models.ImageField(upload_to='place_images')),
            ],
        ),
    ]
