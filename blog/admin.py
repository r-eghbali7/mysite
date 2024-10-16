from django.contrib import admin
from datetime import datetime
from blog.models import post, Category
from django.utils.translation import gettext_lazy as _



# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display = ('title','author','counted_views','status','published_date','created_date')
    list_filter = ('published_date','author')
    #ordering = ('-created_date',)
    search_fields = ('title', 'content')

admin.site.register(post, PostAdmin)
admin.site.register(Category)