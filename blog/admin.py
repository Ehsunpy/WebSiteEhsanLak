from django.contrib import admin

from .models import Post, PostCategory, PostImage


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "accent_color")
    search_fields = ("title", "description")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "status", "published_at", "featured")
    list_filter = ("status", "category", "featured")
    search_fields = ("title", "summary", "content")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PostImageInline]
    ordering = ("-published_at",)
