# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Film(models.Model):
    id_film = models.AutoField(primary_key=True)
    title = models.CharField(blank=True, null=True)
    stars_journalist = models.CharField(max_length=50, blank=True, null=True)
    stars_spectators = models.CharField(max_length=50, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    reference = models.IntegerField(blank=True, null=True)
    id_history = models.ForeignKey('History', models.DO_NOTHING, db_column='id_history')

    class Meta:
        managed = False
        db_table = 'film'


class History(models.Model):
    id_history = models.AutoField(primary_key=True)
    analyze_date = models.DateTimeField(blank=True, null=True)
    validated = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'history'


class JournalistCritics(models.Model):
    id_journalist_critics = models.AutoField(primary_key=True)
    text = models.CharField(blank=True, null=True)
    stars = models.CharField(max_length=50, blank=True, null=True)
    id_film = models.ForeignKey(Film, models.DO_NOTHING, db_column='id_film')

    class Meta:
        managed = False
        db_table = 'journalist_critics'


class ModelBertBmus(models.Model):
    id_bert = models.AutoField(primary_key=True)
    five_stars = models.CharField(max_length=50, blank=True, null=True)
    four_stars = models.CharField(max_length=50, blank=True, null=True)
    three_stars = models.CharField(max_length=50, blank=True, null=True)
    two_stars = models.CharField(max_length=50, blank=True, null=True)
    one_stars = models.CharField(max_length=50, blank=True, null=True)
    id_history = models.ForeignKey(History, models.DO_NOTHING, db_column='id_history')
    id_spectator_critics = models.OneToOneField('SpectatorCritics', models.DO_NOTHING, db_column='id_spectator_critics')

    class Meta:
        managed = False
        db_table = 'model_bert_bmus'


class ModelDistilbertBmcss(models.Model):
    id_distilbert = models.AutoField(primary_key=True)
    positive = models.CharField(max_length=50, blank=True, null=True)
    negative = models.CharField(max_length=50, blank=True, null=True)
    neutral = models.CharField(max_length=50, blank=True, null=True)
    id_history = models.ForeignKey(History, models.DO_NOTHING, db_column='id_history')
    id_spectator_critics = models.OneToOneField('SpectatorCritics', models.DO_NOTHING, db_column='id_spectator_critics')

    class Meta:
        managed = False
        db_table = 'model_distilbert_bmcss'


class SpectatorCritics(models.Model):
    id_spectator_critics = models.AutoField(primary_key=True)
    text = models.CharField(blank=True, null=True)
    stars = models.CharField(max_length=50, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    id_history = models.ForeignKey(History, models.DO_NOTHING, db_column='id_history')
    id_film = models.ForeignKey(Film, models.DO_NOTHING, db_column='id_film')

    class Meta:
        managed = False
        db_table = 'spectator_critics'
