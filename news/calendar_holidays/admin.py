from django.contrib import admin
from calendar_holidays.models import Holidays

class HolidaysAdmin(admin.ModelAdmin):
    list_display = ['holiday', ]
    class Meta:
        fields = '__all__'


admin.site.register(Holidays, HolidaysAdmin)
# Register your models here.
