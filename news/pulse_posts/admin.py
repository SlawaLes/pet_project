from django.contrib import admin
from pulse_posts.models import Post, Investor, Instrument

# class PostAdmin(admin.ModelAdmin):
#     list_display = ['likesCount', 'commentsCount', 'reactionsCount', 'inserted']
#     list_filter = []
#
#     class Meta:
#         fields = '__all__'

# class PostInline(admin.TabularInline):
#     model = Post
#     extra = 0
#     fields = ['text', 'likesCount', 'commentsCount', 'reactionsCount', 'inserted']
#     ordering = ["-inserted"]

# class PostInlineInstr(admin.TabularInline):
#     model = InstrumentPost
#     extra = 0
#     fields = ['post',] # 'likesCount', 'commentsCount', 'reactionsCount', 'inserted']
#     # ordering = ["-inserted"]

@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'profile_tinkoff']
    search_fields = ['nickname', ]
    # inlines = [PostInline]

    class Meta:
        fields = '__all__'


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    # model = Instrument
    list_display = ['name', 'ticker', 'type']
    list_filter = ['type']
    search_fields = ['ticker', 'name']
    # inlines = [PostInlineInstr]
    # list_select_related = ["instrumentpost", ]
    # extra = 0

    class Meta:
        fields = '__all__'
