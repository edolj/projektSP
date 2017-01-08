from django.contrib import admin

# Register your models here.
from .models import Article
from .models import Naprava
from .models import Comment

admin.site.register(Article)
admin.site.register(Naprava)
admin.site.register(Comment)