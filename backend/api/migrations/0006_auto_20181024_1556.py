# Generated by Django 2.1 on 2018-10-24 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20181024_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='object_id',
        ),
        migrations.AddField(
            model_name='activity',
            name='education',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Education'),
        ),
        migrations.AlterField(
            model_name='experiencetechnology',
            name='experience',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Experience'),
        ),
        migrations.AlterField(
            model_name='projecttechnology',
            name='project',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Project'),
        ),
    ]