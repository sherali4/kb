from django.db import models


class Report(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    def __str__(self):
        return self.name

class Period(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='report')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.report.name + "-" + self.name


    class META:
        unique_together = [['report', 'name']]
        db_table = 'hisobot_davrlari'


class Satrlar(models.Model):
    name = models.CharField(max_length=400)
    ulchov_birligi = models.CharField(max_length=100)
    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name="period")

    def __str__(self):
        return self.name
