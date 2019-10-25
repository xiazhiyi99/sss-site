# Generated by Django 2.1 on 2019-10-24 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20191015_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='id',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='group_name',
            field=models.CharField(choices=[('DS', 'DS/DL组'), ('YX', '游戏组'), ('AZ', '安卓组'), ('WA', '网安组')], default='-', max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='student_number',
            field=models.CharField(max_length=9, primary_key=True, serialize=False),
        ),
    ]