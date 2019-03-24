# Generated by Django 2.0.6 on 2018-08-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DublinBusTest', '0005_weatherforecast'),
    ]

    operations = [
        migrations.CreateModel(
            name='Busrouteinfojoined',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('location_text', models.CharField(db_column='LOCATION_TEXT', max_length=100)),
                ('address', models.CharField(blank=True, db_column='ADDRESS', max_length=45, null=True)),
                ('status', models.CharField(blank=True, db_column='STATUS', max_length=45, null=True)),
                ('name', models.CharField(db_column='NAME', max_length=45)),
                ('route_direction', models.CharField(db_column='ROUTE_DIRECTION', max_length=45)),
                ('is_stage_point', models.CharField(blank=True, db_column='IS_STAGE_POINT', max_length=45, null=True)),
                ('stage_number', models.CharField(blank=True, db_column='STAGE_NUMBER', max_length=45, null=True)),
                ('rtpi_destination', models.CharField(blank=True, db_column='RTPI_DESTINATION', max_length=45, null=True)),
                ('sequence_number', models.CharField(blank=True, db_column='SEQUENCE_NUMBER', max_length=45, null=True)),
                ('rtpi_origin', models.CharField(blank=True, db_column='RTPI_ORIGIN', max_length=45, null=True)),
                ('number', models.IntegerField()),
                ('stop_name', models.CharField(max_length=100)),
                ('stop_lat', models.CharField(max_length=45)),
                ('stop_lon', models.CharField(max_length=45)),
                ('stop_id', models.IntegerField()),
            ],
            options={
                'db_table': 'BusRouteInfoJoined',
                'managed': False,
            },
        ),
    ]
