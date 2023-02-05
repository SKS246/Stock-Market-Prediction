# Generated by Django 4.0.2 on 2022-02-20 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0010_rename_reliance_predictions_adani_ports_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predictions',
            name='reliance_ltd',
        ),
        migrations.AddField(
            model_name='predictions',
            name='reliance',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
    ]
