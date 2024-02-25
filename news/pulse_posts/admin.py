from django.contrib import admin
from pulse_posts.models import Post, Investor, Instrument
from django.contrib.admin.views.main import ChangeList

class MyChangeList(ChangeList):
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('total_posts')


class PostInlineInstr(admin.TabularInline):
    model = Post.instrument.through
    extra = 0

    def text_inline(self, obj):
        return obj.post.text
    def date_inline(self, obj):
        return obj.post.inserted

    date_inline.short_description = 'Дата'
    text_inline.short_description = 'Текст постов'

    def get_readonly_fields(self, request, obj=None):
        return list(super().get_readonly_fields(request, obj)) + ['text_inline', 'date_inline']

    def has_change_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)[:1]
        return qs

    #autocomplete_fields = ['text', 'likesCount',] # 'commentsCount', 'reactionsCount', 'inserted']
    #ordering = ["-inserted"]


# class PostInlineInstr(admin.TabularInline):
#     model = InstrumentPost
#     extra = 0
#     fields = ['post',] # 'likesCount', 'commentsCount', 'reactionsCount', 'inserted']
#     # ordering = ["-inserted"]

class PostInlineInv(admin.TabularInline):
    model = Post
    extra = 0
    fields = ['text', 'likesCount', 'commentsCount', 'reactionsCount', 'inserted']
    ordering = ["-inserted"]


@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'profile_tinkoff']
    search_fields = ['nickname', ]
    inlines = [PostInlineInv]

    class Meta:
        fields = '__all__'


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    # model = Instrument
    list_display = ['name', 'ticker', 'type']
    list_filter = ['type']
    search_fields = ['ticker', 'name']
    inlines = [PostInlineInstr]
    # list_select_related = ["instrumentpost", ]
    # extra = 0
    def get_changelist(self, *args, **kwargs):
        return MyChangeList

    class Meta:
        fields = '__all__'
