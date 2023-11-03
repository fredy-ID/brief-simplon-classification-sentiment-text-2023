# Generated by Django 4.2.6 on 2023-11-03 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='history',
            name='id_bert',
        ),
        migrations.RemoveField(
            model_name='history',
            name='id_distilbert',
        ),
        migrations.RemoveField(
            model_name='history',
            name='id_film',
        ),
        migrations.RemoveField(
            model_name='history',
            name='id_spectator_critics',
        ),
        migrations.AddField(
            model_name='film',
            name='id_history',
            field=models.ForeignKey(blank=True, db_column='id_history', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.history'),
        ),
        migrations.AddField(
            model_name='modelbertbmus',
            name='id_history',
            field=models.ForeignKey(blank=True, db_column='id_history', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.history'),
        ),
        migrations.AddField(
            model_name='modeldistilbertbmcss',
            name='id_history',
            field=models.ForeignKey(blank=True, db_column='id_history', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.history'),
        ),
        migrations.AddField(
            model_name='spectatorcritics',
            name='id_history',
            field=models.ForeignKey(blank=True, db_column='id_history', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.history'),
        ),
        migrations.AlterField(
            model_name='film',
            name='reference',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='journalistcritics',
            name='text',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='modelbertbmus',
            name='id_spectator_critics',
            field=models.OneToOneField(db_column='id_spectator_critics', on_delete=django.db.models.deletion.DO_NOTHING, to='api.spectatorcritics'),
        ),
        migrations.AlterField(
            model_name='modeldistilbertbmcss',
            name='id_spectator_critics',
            field=models.OneToOneField(db_column='id_spectator_critics', on_delete=django.db.models.deletion.DO_NOTHING, to='api.spectatorcritics'),
        ),
        migrations.AlterField(
            model_name='spectatorcritics',
            name='text',
            field=models.CharField(blank=True, null=True),
        ),
    ]
