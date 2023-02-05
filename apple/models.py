from django.db import models

# Create your models here.


class predictions(models.Model):
    date = models.TextField(max_length=10)
    tcs = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    reliance = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    asian_paints = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    axis_bank = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    bajaj_auto = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    bajaj_finance = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    bajaj_finserv = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    bharti_airtel = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    bpcl = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    britannia = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    cipla = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    coal_india = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    divis_lab = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    dr_reddys_lab = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    eicher_motor = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    grasim = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    hcl_tech = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    hdfc = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    hdfc_bank = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    hero_motor = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    hindalco = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    hul = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    icici_bank = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    indusind_bank = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    infosys = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    ioc = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    itc = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    jsw_steel = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    kotak_mahindra_bank = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    lnt = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    mnm = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    maruti_suzuki = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    nestle = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    ntpc = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    ongc = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    power_grid = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    sbi = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    sbi_life_insurance = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    shree_cement = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    sun_pharma = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    tata_motors = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    tata_steel = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    tech_mahindra = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    titan = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    ultratech_cement = models.DecimalField(
        decimal_places=10, max_digits=64, default=0)
    upl = models.DecimalField(decimal_places=10, max_digits=64, default=0)
    wipro = models.DecimalField(decimal_places=10, max_digits=64, default=0)
