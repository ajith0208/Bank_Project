from django.contrib import admin
from .models import District, Branch, Application


# Register your models here.

class DistrictAdmin(admin.ModelAdmin):
    List_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(District, DistrictAdmin)


class BranchAdmin(admin.ModelAdmin):
    List_display = ['name', 'slug', 'district']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Branch, BranchAdmin)


class ApplicationAdmin(admin.ModelAdmin):
    List_display = ['name', 'age', 'district', 'branch', 'account']


admin.site.register(Application, ApplicationAdmin)
