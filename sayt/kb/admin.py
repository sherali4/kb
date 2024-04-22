from django.contrib import admin
from .models import Report, Period, Satrlar



class ReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Report, ReportAdmin)

class PeriodAdmin(admin.ModelAdmin):
    list_display = ('name', 'report')

admin.site.register(Period, PeriodAdmin)
class SatrlarAdmin(admin.ModelAdmin):
    list_display = ('name', 'period')

admin.site.register(Satrlar, SatrlarAdmin)
