from django.contrib import admin
from .models import Countries, Categories, RequestParamsTopLines, TopNews

class CountryAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'

class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'


class RequestParamsTopLinesAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'


class TopNewsAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'


admin.site.register(TopNews, TopNewsAdmin)
admin.site.register(Countries, CountryAdmin)
admin.site.register(Categories, CategoryAdmin)
admin.site.register(RequestParamsTopLines, RequestParamsTopLinesAdmin)

# Register your models here.
