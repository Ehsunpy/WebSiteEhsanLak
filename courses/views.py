from django.views.generic import DetailView, ListView

from .models import Course, CourseCategory


class CourseListView(ListView):
    model = Course
    template_name = "courses/list.html"
    context_object_name = "courses"

    def get_queryset(self):
        queryset = Course.objects.filter(published=True).order_by("display_order")
        category_slug = self.request.GET.get("category")
        level = self.request.GET.get("level")

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        if level:
            queryset = queryset.filter(level=level)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = CourseCategory.objects.all()
        context["active_category"] = self.request.GET.get("category")
        context["active_level"] = self.request.GET.get("level")
        return context


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_courses"] = (
            Course.objects.filter(category=self.object.category, published=True)
            .exclude(pk=self.object.pk)[:3]
        )
        return context
