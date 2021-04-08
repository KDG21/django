from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Covid19(models.Model):
    accdefrate     = models.FloatField(db_column='accDefRate', blank=True, null=True, max_length=15)
    accexamcnt     = models.IntegerField(db_column='accExamCnt', blank=True, null=True)
    accexamcompcnt = models.IntegerField(db_column='accExamCompCnt', blank=True, null=True)
    carecnt        = models.IntegerField(db_column='careCnt', blank=True, null=True)
    clearcnt       = models.IntegerField(db_column='clearCnt', blank=True, null=True)
    createdt       = models.DateTimeField(db_column='createDt', blank=True, null=True)
    deathcnt       = models.IntegerField(db_column='deathCnt', blank=True, null=True)
    decidecnt      = models.IntegerField(db_column='decideCnt', blank=True, null=True)
    examcnt        = models.IntegerField(db_column='examCnt', blank=True, null=True)
    resutlnegcnt   = models.IntegerField(db_column='resutlNegCnt', blank=True, null=True)
    seq            = models.IntegerField(blank=True, null=True)
    statedt        = models.DateField(db_column='stateDt', blank=True, null=True)
    statetime      = models.TimeField(db_column='stateTime', blank=True, null=True, max_length=4)
    updatedt       = models.DateTimeField(db_column='updateDt', blank=True, null=True, max_length=4)