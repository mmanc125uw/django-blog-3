# blogging/admin.py
from django.contrib import admin
from blogging.models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
    
    exclude = ('posts', )

admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)
