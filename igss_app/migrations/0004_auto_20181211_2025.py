# Generated by Django 2.1.2 on 2018-12-11 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('igss_app', '0003_meetingagenda'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetingagenda',
            old_name='creator_id',
            new_name='creator',
        ),
    ]
