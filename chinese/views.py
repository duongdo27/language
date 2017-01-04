import json

from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Ideograph, Story, Example, Deck, DeckIdeograph, Component, Proficiency
from .helper import generate_quiz_data


class HomeView(TemplateView):
    template_name = 'index.html'


class IdeographDetailView(DetailView):
    model = Ideograph
    template_name = 'ideograph.html'

    def get_context_data(self, **kwargs):
        context = super(IdeographDetailView, self).get_context_data(**kwargs)
        context['components'] = [x.component for x in Component.objects.filter(ideograph=self.object)]
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

        proficiency = Proficiency.objects.filter(user=self.request.user)
        proficiency_lookup = {x.ideograph: x.score for x in proficiency}

        ls = DeckIdeograph.objects.filter(deck=self.object).order_by('position')

        data = {}
        for deck_ideograph in ls:
            lesson = deck_ideograph.lesson
            row = (deck_ideograph.ideograph, proficiency_lookup.get(deck_ideograph.ideograph, 0))
            if lesson in data:
                data[lesson].append(row)
            else:
                data[lesson] = [row]

        context['data'] = data.items()
        return context


class QuizView(TemplateView):
    template_name = "quiz.html"

    def get_context_data(self, **kwargs):
        context = super(QuizView, self).get_context_data(**kwargs)
        context['data'] = json.dumps(generate_quiz_data(kwargs.get('deck_id'), kwargs.get('lesson')))
        return context
