# Generated by Django 4.0.2 on 2022-02-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0009_rename_tcs_predictions_tcs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predictions',
            old_name='reliance',
            new_name='adani_ports',
        ),
        migrations.AddField(
            model_name='predictions',
            name='asian_paints',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='axis_bank',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='reliance_ltd',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
    ]
