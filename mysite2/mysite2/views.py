from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        cotext = super().get_context_data(**kwargs)
        cotext['app_list'] = ['polls', 'books']
        return cotext