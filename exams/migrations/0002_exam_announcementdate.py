# Generated by Django 3.0b1 on 2019-11-18 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='announcementDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
