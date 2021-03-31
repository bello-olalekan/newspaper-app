# articles/admin.py
from django.contrib import admin
from .models import Article, Comment



class CommentInline(admin.TabularInline): # new
    model = Comment

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class CommentInline(admin.StackedInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)