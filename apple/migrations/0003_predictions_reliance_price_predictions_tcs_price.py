# Generated by Django 4.0.2 on 2022-02-19 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0002_rename_predicted_price_predictions_apple_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictions',
            name='reliance_price',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='tcs_price',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=64),
        ),
    ]
