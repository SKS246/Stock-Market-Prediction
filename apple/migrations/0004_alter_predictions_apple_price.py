# Generated by Django 4.0.2 on 2022-02-19 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0003_predictions_reliance_price_predictions_tcs_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions',
            name='apple_price',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=64),
        ),
    ]
