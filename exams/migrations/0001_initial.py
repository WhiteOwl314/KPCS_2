# Generated by Django 3.0b1 on 2019-11-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('examDate', models.DateField()),
                ('receptionDate_created', models.DateField()),
                ('receptionDate_ended', models.DateField()),
            ],
        ),
    ]
