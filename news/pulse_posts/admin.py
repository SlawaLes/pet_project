from django.contrib import admin
from pulse_posts.models import PostsTicker

class PostsTickerAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'ticker', 'likesCount', 'commentsCount', 'inserted']
    list_filter = ['ticker', ]

    class Meta:
        fields = '__all__'

admin.site.register(PostsTicker, PostsTickerAdmin)

# Register your models here.
