# Generated by Django 2.1.2 on 2018-12-12 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('igss_app', '0008_agenda_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingagenda',
            name='agenda_state_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='igss_app.Agenda_State'),
        ),
    ]
