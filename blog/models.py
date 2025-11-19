from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField


class PostCategory(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)
    accent_color = models.CharField(max_length=10, default="#ff5d8f")

    class Meta:
        verbose_name = "دسته‌بندی بلاگ"
        verbose_name_plural = "دسته‌بندی‌های بلاگ"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Post(models.Model):
    STATUS_CHOICES = [("draft", "پیش‌نویس"), ("published", "منتشر شده")]

    category = models.ForeignKey(
        PostCategory, related_name="posts", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    hero_image = models.ImageField(upload_to="blog/hero/", blank=True, null=True)
    cover_tone = models.CharField(max_length=10, default="#312e81")
    summary = models.TextField(max_length=400)
    content = RichTextField()
    tags = models.CharField(max_length=250, blank=True, help_text="با کاما جدا کنید")
    reading_time = models.PositiveSmallIntegerField(default=5)
    author_name = models.CharField(max_length=120, default="احسان لک")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    published_at = models.DateTimeField(default=timezone.now)
    featured = models.BooleanField(default=False)
    seo_description = models.CharField(max_length=160, blank=True)

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "پست"
        verbose_name_plural = "پست‌ها"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                counter += 1
                slug = f"{base_slug}-{counter}"
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

    @property
    def tag_list(self):
        if not self.tags:
            return []
        return [tag.strip() for tag in self.tags.split(",") if tag.strip()]


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name="gallery", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog/gallery/")
    caption = models.CharField(max_length=120, blank=True)

    class Meta:
        verbose_name = "تصویر پست"
        verbose_name_plural = "تصاویر پست"

    def __str__(self):
        return f"تصویر {self.post.title}"
