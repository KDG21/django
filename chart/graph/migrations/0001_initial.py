# Generated by Django 3.1.7 on 2021-04-08 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Covid19',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accdefrate', models.FloatField(blank=True, db_column='accDefRate', max_length=15, null=True)),
                ('accexamcnt', models.IntegerField(blank=True, db_column='accExamCnt', null=True)),
                ('accexamcompcnt', models.IntegerField(blank=True, db_column='accExamCompCnt', null=True)),
                ('carecnt', models.IntegerField(blank=True, db_column='careCnt', null=True)),
                ('clearcnt', models.IntegerField(blank=True, db_column='clearCnt', null=True)),
                ('createdt', models.DateTimeField(blank=True, db_column='createDt', null=True)),
                ('deathcnt', models.IntegerField(blank=True, db_column='deathCnt', null=True)),
                ('decidecnt', models.IntegerField(blank=True, db_column='decideCnt', null=True)),
                ('examcnt', models.IntegerField(blank=True, db_column='examCnt', null=True)),
                ('resutlnegcnt', models.IntegerField(blank=True, db_column='resutlNegCnt', null=True)),
                ('seq', models.IntegerField(blank=True, null=True)),
                ('statedt', models.DateField(blank=True, db_column='stateDt', null=True)),
                ('statetime', models.TimeField(blank=True, db_column='stateTime', max_length=4, null=True)),
                ('updatedt', models.DateTimeField(blank=True, db_column='updateDt', max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('population', models.PositiveIntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graph.country')),
            ],
        ),
    ]
