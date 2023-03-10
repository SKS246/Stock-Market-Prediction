# Generated by Django 4.0.2 on 2022-02-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0012_remove_predictions_adani_ports'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictions',
            name='bajaj_auto',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='bajaj_finance',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='bajaj_finserv',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='bharti_airtel',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='bpcl',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='britannia',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='cipla',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='coal_india',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='divis_lab',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='dr_reddys_lab',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='eicher_motor',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='grasim',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='hcl_tech',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='hdfc',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='hdfc_bank',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='hdfc_life_insurance',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='hero_motor',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='hindalco',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='hul',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='icici_bank',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='indusind_bank',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='infosys',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='ioc',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='itc',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='jsw_steel',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='kotak_mahindra_bank',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='lnt',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='maruti_suzuki',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='mnm',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='nestle',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='ntpc',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='ongc',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='power_grid',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='sbi',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='sbi_life_insurance',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='shree_cement',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='sun_pharma',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='tata_consumers',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='tata_motors',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='tata_steel',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='tech_mahindra',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='titan',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='ultratech_cement',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='upl',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='predictions',
            name='wipro',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=64),
        ),
    ]
