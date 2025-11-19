from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from blog.models import Post
from courses.models import Course
from .forms import ContactForm
from .models import ActivitySpotlight, Experience, MetricBadge, Recognition, Skill


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["experiences"] = Experience.objects.all()
        context["skills"] = Skill.objects.all()
        context["activities"] = ActivitySpotlight.objects.all()
        context["recognitions"] = Recognition.objects.all()
        context["metrics"] = MetricBadge.objects.all()
        context["featured_posts"] = Post.objects.filter(status="published")[:4]
        context["featured_courses"] = Course.objects.filter(
            published=True
        ).order_by("display_order")[:3]
        context["contact_form"] = ContactForm()
        return context


class AboutView(TemplateView):
    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["experiences"] = Experience.objects.all()
        context["recognitions"] = Recognition.objects.all()
        return context


class ContactView(FormView):
    template_name = "core/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("core:contact")

    def form_valid(self, form):
        topic = form.cleaned_data.get("topic") or "بدون موضوع"
        body = (
            f"نام: {form.cleaned_data['name']}\n"
            f"ایمیل: {form.cleaned_data['email']}\n"
            f"موضوع: {topic}\n\n"
            f"{form.cleaned_data['message']}"
        )
        send_mail(
            subject=f"پیام جدید از {form.cleaned_data['name']} | {topic}",
            message=body,
            from_email=form.cleaned_data["email"],
            recipient_list=["hello@ehsanlak.dev"],
            fail_silently=True,
        )
        messages.success(self.request, "پیام شما با موفقیت ارسال شد.")
        return super().form_valid(form)
