# Generated by Django 2.1 on 2019-10-15 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0002_auto_20191005_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='publisher',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
