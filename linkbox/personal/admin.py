from django.contrib import admin
from .models import UserDetail, Link, Category, Tag, UserLink, LinkComment

class CommentInline(admin.TabularInline):
    model = LinkComment
    extra = 3

class UserLinkAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]

admin.site.register(UserDetail)
admin.site.register(Link)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(UserLink, UserLinkAdmin)
