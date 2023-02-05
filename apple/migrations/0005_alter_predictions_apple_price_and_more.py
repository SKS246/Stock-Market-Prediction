# Generated by Django 4.0.2 on 2022-02-19 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0004_alter_predictions_apple_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions',
            name='apple_price',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='reliance_price',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='tcs_price',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
    ]
