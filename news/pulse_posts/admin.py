from django.contrib import admin
from pulse_posts.models import Post, Investor, Instrument

# class PostAdmin(admin.ModelAdmin):
#     list_display = ['likesCount', 'commentsCount', 'reactionsCount', 'inserted']
#     list_filter = []
#
#     class Meta:
#         fields = '__all__'

class PostInline(admin.TabularInline):
    model = Post
    extra = 0
    fields = ['text', 'likesCount', 'commentsCount', 'reactionsCount', 'inserted']

class InvestorAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'profile_tinkoff']
    list_filter = []
    inlines = [PostInline]

    class Meta:
        fields = '__all__'



class InstrumentAdmin(admin.ModelAdmin):
    # model = Instrument
    list_display = ['name', 'ticker', 'type']
    list_filter = ['type']
    search_fields = ['ticker', 'name']

    # extra = 0

    class Meta:
        fields = '__all__'

# Register your models here.
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Investor, InvestorAdmin)
# admin.site.register(Post, PostAdmin)