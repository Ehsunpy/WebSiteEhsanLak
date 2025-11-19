from django.contrib import admin

from .models import ActivitySpotlight, Experience, MetricBadge, Recognition, Skill


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "organization", "start_date", "end_date", "is_current")
    list_filter = ("is_current", "organization")
    search_fields = ("role", "organization", "description")
    ordering = ("weight", "-start_date")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "level")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(ActivitySpotlight)
class ActivitySpotlightAdmin(admin.ModelAdmin):
    list_display = ("title", "cta_label", "cta_link")
    search_fields = ("title", "description")


@admin.register(Recognition)
class RecognitionAdmin(admin.ModelAdmin):
    list_display = ("title", "issuer", "year")
    search_fields = ("title", "issuer")


@admin.register(MetricBadge)
class MetricBadgeAdmin(admin.ModelAdmin):
    list_display = ("label", "value", "suffix")
    search_fields = ("label",)
