from django.contrib import admin

# Register your models here.
from .models import Article, Naprava, Comment

admin.site.register(Article)
admin.site.register(Naprava)
admin.site.register(Comment)