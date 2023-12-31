# Generated by Django 4.2.6 on 2023-11-03 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_journalistcritics_id_film_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id_history', models.AutoField(primary_key=True, serialize=False)),
                ('analyze_date', models.DateTimeField(blank=True, null=True)),
                ('validated', models.BooleanField(blank=True, null=True)),
                ('id_bert', models.ForeignKey(blank=True, db_column='id_bert', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.modelbertbmus')),
                ('id_distilbert', models.ForeignKey(blank=True, db_column='id_distilbert', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.modeldistilbertbmcss')),
                ('id_film', models.ForeignKey(blank=True, db_column='id_film', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.film')),
                ('id_spectator_critics', models.ForeignKey(blank=True, db_column='id_spectator_critics', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.spectatorcritics')),
            ],
            options={
                'db_table': 'history',
            },
        ),
    ]
