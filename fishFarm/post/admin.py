from django.contrib import admin
from .models import Dam, New_department, Staff, Fish

# Register your models here.
class DamAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dam, DamAdmin)

class New_departmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(New_department, New_departmentAdmin)

class StaffAdmin(admin.ModelAdmin):
    pass

admin.site.register(Staff, StaffAdmin)

class FishAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fish, FishAdmin)




