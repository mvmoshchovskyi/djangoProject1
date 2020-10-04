# Generated by Django 3.1.2 on 2020-10-04 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201004_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='moviemodel',
            name='description',
            field=models.TextField(default='DEFAULT VALUE', max_length=500),
        ),
        migrations.AddField(
            model_name='moviemodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterModelTable(
            name='moviemodel',
            table='movie',
        ),
    ]