# Generated by Django 2.1 on 2018-10-25 03:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_workflow'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='visit_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]