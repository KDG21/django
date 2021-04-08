from django.db import models


class Covid19(models.Model):
    createdt = models.DateTimeField(db_column='createDt', blank=True, null=True)  # Field name made lowercase.
    decidecnt = models.IntegerField(db_column='decideCnt', blank=True, null=True)  # Field name made lowercase.
    deathcnt = models.IntegerField(db_column='deathCnt', blank=True, null=True)  # Field name made lowercase.
    accexamcompcnt = models.IntegerField(db_column='accExamCompCnt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'covid19'