# Generated by Django 2.1 on 2018-10-25 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_guest_visit_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.CharField(max_length=20),
        ),
    ]
