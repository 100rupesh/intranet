# Generated by Django 3.1.5 on 2021-05-20 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_conveyance_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='conveyance',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='events/'),
        ),
    ]
