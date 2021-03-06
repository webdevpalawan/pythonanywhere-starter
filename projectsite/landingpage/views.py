from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "landingpage/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "My Legit HomePage"
        return context
