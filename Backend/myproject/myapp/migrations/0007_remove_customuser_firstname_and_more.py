# Generated by Django 5.1.3 on 2024-11-17 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_fullname_customuser_firstname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='lastname',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
