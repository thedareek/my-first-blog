from django.contrib import admin

from blog.models import Article, Comments

admin.site.register(Article)
admin.site.register(Comments)
