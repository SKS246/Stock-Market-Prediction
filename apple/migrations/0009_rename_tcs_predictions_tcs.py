# Generated by Django 4.0.2 on 2022-02-20 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0008_rename_reliance_predictions_reliance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predictions',
            old_name='TCS',
            new_name='tcs',
        ),
    ]
