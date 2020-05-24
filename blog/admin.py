from django.contrib import admin
from .models import Block,Article
@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('tag','content')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('time','title','intro','img','imgInf')
# Register your models here.
