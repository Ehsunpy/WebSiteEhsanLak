from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField


class CourseCategory(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=100, blank=True)
    accent_color = models.CharField(max_length=10, default="#f97316")

    class Meta:
        verbose_name = "دسته‌بندی دوره"
        verbose_name_plural = "دسته‌بندی‌های دوره"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Course(models.Model):
    LEVEL_CHOICES = [
        ("intro", "مقدماتی"),
        ("intermediate", "میان‌رده"),
        ("advanced", "پیشرفته"),
    ]

    category = models.ForeignKey(
        CourseCategory, related_name="courses", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=240, unique=True, blank=True)
    summary = models.TextField(max_length=500)
    description = RichTextField()
    hero_image = models.ImageField(upload_to="courses/hero/", blank=True, null=True)
    featured_video_url = models.URLField(blank=True)
    duration = models.CharField(max_length=60, default="10 ساعت")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default="intro")
    price = models.PositiveIntegerField(default=0, help_text="به تومان")
    include_certificate = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    accent_color = models.CharField(max_length=10, default="#a855f7")
    syllabus_outline = models.TextField(blank=True)
    display_order = models.PositiveSmallIntegerField(default=1)
    seo_description = models.CharField(max_length=160, blank=True)

    class Meta:
        ordering = ["display_order", "title"]
        verbose_name = "دوره"
        verbose_name_plural = "دوره‌ها"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("courses:detail", kwargs={"slug": self.slug})


class CourseResource(models.Model):
    RESOURCE_TYPES = [
        ("pdf", "PDF"),
        ("doc", "Word"),
        ("image", "تصویر"),
        ("video", "ویدیو"),
        ("other", "سایر"),
    ]

    course = models.ForeignKey(
        Course, related_name="resources", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to="courses/resources/")
    resource_type = models.CharField(
        max_length=10, choices=RESOURCE_TYPES, default="pdf"
    )
    description = models.CharField(max_length=200, blank=True)
    is_downloadable = models.BooleanField(default=True)

    class Meta:
        verbose_name = "منبع دوره"
        verbose_name_plural = "منابع دوره"

    def __str__(self):
        return f"{self.course.title} - {self.title}"
