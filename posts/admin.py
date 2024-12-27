from django.contrib import admin
from posts.models import Post, Category, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'rate',
        'created_at',
        'updated_at',
        'category'
    )
    list_filter = ('created_at', 'updated_at', 'category')
    search_fields = ('title', 'description')
    list_editable = ('rate',)


admin.site.register(Category)
admin.site.register(Tag)