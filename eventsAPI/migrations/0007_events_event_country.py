# Generated by Django 4.2.3 on 2023-07-09 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsAPI', '0006_alter_events_created_at_alter_events_event_lat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_country',
            field=models.CharField(default='jordan', max_length=64),
        ),
    ]
