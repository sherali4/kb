from django.contrib import admin

from .models import Hisobotlar, Muddati, Xat_turi, Baza


class HisobotlarAdmin(admin.ModelAdmin):
    list_display = ('name', 'izoh')
admin.site.register(Hisobotlar, HisobotlarAdmin)


class MuddatiAdmin(admin.ModelAdmin):
    list_display = ('title', 'hisobot')
admin.site.register(Muddati, MuddatiAdmin)



class Xat_turiAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(Xat_turi, Xat_turiAdmin)



class BazaAdmin(admin.ModelAdmin):
    list_display = ('okpo', 'inn', 'nomi', 'soato4')
    # readonly_fields = ['soato4', 'soato7']
admin.site.register(Baza, BazaAdmin)


