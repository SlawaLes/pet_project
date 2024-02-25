from django.contrib import admin
from pulse_posts.models import Post, Investor, Instrument
from django_admin_inline_paginator.admin import TabularInlinePaginated


class PostInlineInstr(TabularInlinePaginated):
    model = Post.instrument.through
    per_page = 3

    def date_inline(self, obj):
        return obj.post.inserted
    date_inline.short_description = 'Дата'

    def get_readonly_fields(self, request, obj=None):
        return list(super().get_readonly_fields(request, obj)) + ['date_inline',]

    def has_change_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('post').order_by('-post__inserted')


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
    list_display = ['name', 'ticker', 'type']
    list_filter = ['type']
    search_fields = ['ticker', 'name']
    inlines = [PostInlineInstr]

    class Meta:
        fields = '__all__'
