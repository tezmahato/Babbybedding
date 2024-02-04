from django.contrib import admin

# Register your models here.
from service.models import service

class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_descrip')


admin.site.register(service,ServiceAdmin)