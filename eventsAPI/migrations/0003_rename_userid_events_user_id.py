# Generated by Django 4.2.3 on 2023-07-09 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventsAPI', '0002_rename_event_lan_events_event_lon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='userID',
            new_name='user_id',
        ),
    ]