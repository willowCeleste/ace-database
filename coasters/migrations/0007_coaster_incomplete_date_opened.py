# Generated by Django 3.2.12 on 2022-03-07 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coasters', '0006_alter_coaster_date_opened'),
    ]

    operations = [
        migrations.AddField(
            model_name='coaster',
            name='incomplete_date_opened',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
