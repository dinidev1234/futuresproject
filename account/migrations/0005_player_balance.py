# Generated by Django 5.0 on 2023-12-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_player_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
