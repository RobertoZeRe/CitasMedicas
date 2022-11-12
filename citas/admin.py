from django.contrib import admin
from .models import Citas
from .models import Especialidad

class CitasAdmin(admin.ModelAdmin):
    readonly_fields = ("creado",)




# Register your models here.
admin.site.register(Citas, CitasAdmin)
admin.site.register(Especialidad)
