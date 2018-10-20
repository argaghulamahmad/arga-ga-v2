# Generated by Django 2.1.2 on 2018-10-20 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_social'),
    ]

    operations = [
        migrations.RenameField(
            model_name='social',
            old_name='subject',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='social',
            name='body',
        ),
        migrations.AddField(
            model_name='social',
            name='link',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
