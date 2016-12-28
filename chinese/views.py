from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Ideograph, Story, Example, Deck


class HomeView(TemplateView):
    template_name = 'index.html'


class IdeographDetailView(DetailView):
    model = Ideograph
    template_name = 'ideograph.html'

    def get_context_data(self, **kwargs):
        context = super(IdeographDetailView, self).get_context_data(**kwargs)
        context['stories'] = Story.objects.filter(ideograph=self.object).order_by('position')
        context['examples'] = Example.objects.filter(ideograph=self.object).order_by('position')
        return context


class DeckListView(ListView):
    model = Deck
    template_name = 'deck_list.html'


class DeckDetailView(DetailView):
    model = Deck
    template_name = "deck.html"

    def get_context_data(self, **kwargs):
        context = super(DeckDetailView, self).get_context_data(**kwargs)
        return context

