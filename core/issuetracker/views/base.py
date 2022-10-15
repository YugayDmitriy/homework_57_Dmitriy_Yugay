from django.views.generic import TemplateView
from issuetracker.models import Issue


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = Issue.objects.all()
        return context
