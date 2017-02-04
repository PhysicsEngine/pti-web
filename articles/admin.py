from django.contrib import admin

from .models import Authors
from .models import Articles

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rate')

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_date', 'url', 'get_author')
    
    def get_author(self, obj):
        return obj.author.name

admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Articles, ArticlesAdmin)
