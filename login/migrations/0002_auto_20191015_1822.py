# Generated by Django 2.1 on 2019-10-15 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='student_number',
            field=models.CharField(max_length=9),
        ),
    ]
