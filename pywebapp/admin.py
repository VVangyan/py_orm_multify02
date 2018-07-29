from django.contrib import admin
from pywebapp import models


# Register your models here.

# 自定义一些操作
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'pub_date')
    list_editable = ('name', 'price')
    filter_horizontal = ('authors',)  # 垂直 水平的 搜索  ()filter_vertical =
    list_per_page = 2
    search_fields = ('id', 'name', 'publish__name')#搜索
    list_filter = ('pub_date', 'publish')#过滤器


# 注册
admin.site.register(models.Author)
admin.site.register(models.Publish)
admin.site.register(models.Book, BookAdmin)  # 注册到
