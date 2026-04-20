from django.contrib import admin

from .models import Post, Category, Location


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
        'pub_date',
        'category',
        'author',
        'location'
    )
    list_editable = (
        'is_published',
        'category'
    )
    search_fields = ('title', 'author__username')
    list_filter = (
        'category',
        'author',
        'location'
    )
    list_display_links = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    search_fields = ('name',)
