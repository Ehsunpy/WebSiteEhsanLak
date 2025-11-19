from django.db.models import Q
from django.views.generic import DetailView, ListView

from .models import Post, PostCategory


class BlogListView(ListView):
    model = Post
    template_name = "blog/list.html"
    paginate_by = 6
    context_object_name = "posts"

    def get_queryset(self):
        queryset = Post.objects.filter(status="published")
        category_slug = self.request.GET.get("category")
        search = self.request.GET.get("q")

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search)
                | Q(summary__icontains=search)
                | Q(content__icontains=search)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = PostCategory.objects.all()
        context["active_category"] = self.request.GET.get("category")
        context["search_query"] = self.request.GET.get("q", "")
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_posts"] = (
            Post.objects.filter(category=self.object.category)
            .exclude(pk=self.object.pk)
            .filter(status="published")[:3]
        )
        return context
