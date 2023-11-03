# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Film(models.Model):
    id_film = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    stars_journalist = models.CharField(max_length=50, blank=True, null=True)
    stars_spectators = models.CharField(max_length=50, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    reference = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        db_table = 'film'


class JournalistCritics(models.Model):
    id_journalist_critics = models.AutoField(primary_key=True)
    text = models.CharField(max_length=50, blank=True, null=True)
    stars = models.CharField(max_length=50, blank=True, null=True)
    id_film = models.ForeignKey(Film, models.DO_NOTHING, db_column='id_film')

    class Meta:
        db_table = 'journalist_critics'


class ModelBertBmus(models.Model):
    id_bert = models.AutoField(primary_key=True)
    five_stars = models.CharField(max_length=50, blank=True, null=True)
    four_stars = models.CharField(max_length=50, blank=True, null=True)
    three_stars = models.CharField(max_length=50, blank=True, null=True)
    two_stars = models.CharField(max_length=50, blank=True, null=True)
    one_stars = models.CharField(max_length=50, blank=True, null=True)
    id_spectator_critics = models.ForeignKey('SpectatorCritics', models.DO_NOTHING, db_column='id_spectator_critics')

    class Meta:
        db_table = 'model_bert_bmus'


class ModelDistilbertBmcss(models.Model):
    id_distilbert = models.AutoField(primary_key=True)
    positive = models.CharField(max_length=50, blank=True, null=True)
    negative = models.CharField(max_length=50, blank=True, null=True)
    neutral = models.CharField(max_length=50, blank=True, null=True)
    id_spectator_critics = models.ForeignKey('SpectatorCritics', models.DO_NOTHING, db_column='id_spectator_critics')

    class Meta:
        db_table = 'model_distilbert_bmcss'


class SpectatorCritics(models.Model):
    id_spectator_critics = models.AutoField(primary_key=True)
    text = models.CharField(max_length=50, blank=True, null=True)
    stars = models.CharField(max_length=50, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    id_film = models.ForeignKey(Film, models.DO_NOTHING, db_column='id_film')

    class Meta:
        db_table = 'spectator_critics'

class History(models.Model):
    id_history = models.AutoField(primary_key=True)
    analyze_date = models.DateTimeField(blank=True, null=True)
    validated = models.BooleanField(blank=True, null=True)
    id_distilbert = models.ForeignKey('ModelDistilbertBmcss', models.DO_NOTHING, db_column='id_distilbert', blank=True, null=True)
    id_bert = models.ForeignKey('ModelBertBmus', models.DO_NOTHING, db_column='id_bert', blank=True, null=True)
    id_spectator_critics = models.ForeignKey('SpectatorCritics', models.DO_NOTHING, db_column='id_spectator_critics', blank=True, null=True)
    id_film = models.ForeignKey(Film, models.DO_NOTHING, db_column='id_film', blank=True, null=True)

    class Meta:
        db_table = 'history'
