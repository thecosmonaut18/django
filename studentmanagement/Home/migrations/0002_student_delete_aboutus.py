# Generated by Django 4.2.7 on 2024-01-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=30)),
                ('deprt', models.CharField(choices=[('CS', 'Computer Science'), ('IT', 'Information Technology')], max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='AboutUs',
        ),
    ]
