# Generated by Django 4.2.6 on 2023-11-03 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalistcritics',
            name='id_film',
            field=models.ForeignKey(db_column='reference', on_delete=django.db.models.deletion.DO_NOTHING, to='api.film'),
        ),
        migrations.AlterField(
            model_name='spectatorcritics',
            name='id_film',
            field=models.ForeignKey(db_column='reference', on_delete=django.db.models.deletion.DO_NOTHING, to='api.film'),
        ),
    ]
