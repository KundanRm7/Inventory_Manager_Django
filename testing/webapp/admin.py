from django.contrib import admin
from .models import Asset, Category, Manufacturer, Department, Employee, Status, Attachement, Maintenance
# Register your models here.

admin.site.register(Asset)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Department)
admin.site.register(Status)
admin.site.register(Employee)
admin.site.register(Attachement)
admin.site.register(Maintenance)