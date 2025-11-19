from django.contrib import admin

from .models import Course, CourseCategory, CourseResource


class CourseResourceInline(admin.TabularInline):
    model = CourseResource
    extra = 1


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "accent_color")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "level", "price", "published", "is_featured")
    list_filter = ("category", "level", "published", "is_featured")
    search_fields = ("title", "summary", "description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [CourseResourceInline]
    ordering = ("display_order", "title")
