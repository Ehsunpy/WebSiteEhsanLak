from django.db import models


class Experience(models.Model):
    role = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    highlight_color = models.CharField(max_length=10, default="#7c3aed")
    weight = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["weight", "-start_date"]
        verbose_name = "تجربه"
        verbose_name_plural = "تجربه‌ها"

    def __str__(self):
        return f"{self.role} - {self.organization}"


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("ai", "هوش مصنوعی"),
        ("backend", "بک‌اند"),
        ("frontend", "فرانت‌اند"),
        ("devops", "دواپس"),
        ("soft", "مهارت نرم"),
    ]

    name = models.CharField(max_length=80)
    level = models.PositiveSmallIntegerField(default=80)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="ai")
    icon = models.CharField(max_length=100, blank=True)
    accent_color = models.CharField(max_length=10, default="#f97316")

    class Meta:
        ordering = ["-level"]
        verbose_name = "مهارت"
        verbose_name_plural = "مهارت‌ها"

    def __str__(self):
        return self.name


class ActivitySpotlight(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    cta_label = models.CharField(max_length=80, blank=True)
    cta_link = models.URLField(blank=True)
    accent_color = models.CharField(max_length=10, default="#0ea5e9")
    background_image = models.ImageField(
        upload_to="activities/backgrounds/", blank=True, null=True
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "قاب فعالیت"
        verbose_name_plural = "قاب‌های فعالیت"

    def __str__(self):
        return self.title


class Recognition(models.Model):
    title = models.CharField(max_length=150)
    issuer = models.CharField(max_length=150)
    year = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    badge_color = models.CharField(max_length=10, default="#10b981")

    class Meta:
        verbose_name = "موفقیت"
        verbose_name_plural = "موفقیت‌ها"

    def __str__(self):
        return f"{self.title} - {self.issuer}"


class MetricBadge(models.Model):
    label = models.CharField(max_length=80)
    value = models.PositiveIntegerField(default=0)
    suffix = models.CharField(max_length=20, blank=True)
    accent_color = models.CharField(max_length=10, default="#f97316")
    icon = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "شاخص"
        verbose_name_plural = "شاخص‌ها"

    def __str__(self):
        suffix = self.suffix or ""
        return f"{self.value}{suffix} {self.label}"
