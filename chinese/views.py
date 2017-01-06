import json

from django.views.generic import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

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

    def get_context_data(self, **kwargs):
        context = super(DeckListView, self).get_context_data(**kwargs)

        proficiency_objects = Proficiency.objects.filter(user=self.request.user)
        proficiency_lookup = {x.ideograph: x.score for x in proficiency_objects}

        data = []
        for deck in context['object_list']:
            ideographs = [x.ideograph for x in DeckIdeograph.objects.filter(deck=deck)]
            proficiency = sum([proficiency_lookup.get(x, 0) for x in ideographs]) / len(ideographs)
            data.append((deck, proficiency))

        context['data'] = data
        return context


class DeckDetailView(DetailView):
    model = Deck
    template_name = "deck.html"

    def get_context_data(self, **kwargs):
        context = super(DeckDetailView, self).get_context_data(**kwargs)

        proficiency_objects = Proficiency.objects.filter(user=self.request.user)
        proficiency_lookup = {x.ideograph: x.score for x in proficiency_objects}

        deck_ideographs = DeckIdeograph.objects.filter(deck=self.object).order_by('position')

        data = {}
        total = 0
        for deck_ideograph in deck_ideographs:
            lesson = deck_ideograph.lesson
            proficiency = proficiency_lookup.get(deck_ideograph.ideograph, 0)
            row = (deck_ideograph.ideograph, proficiency)
            if lesson in data:
                data[lesson].append(row)
            else:
                data[lesson] = [row]
            total += proficiency

        context['data'] = data.items()
        context['avg_proficiency'] = total / len(deck_ideographs)
        return context


class QuizView(TemplateView):
    template_name = "quiz.html"

    def get_context_data(self, **kwargs):
        context = super(QuizView, self).get_context_data(**kwargs)
        context['data'] = json.dumps(generate_quiz_data(kwargs.get('deck_id'), kwargs.get('lesson')))
        # context['success_url'] = '/deck/{}'.format(kwargs.get('deck_id'))
        context['success_url'] = reverse_lazy('chinese:deck', kwargs={'pk': kwargs.get('deck_id')})
        return context


@method_decorator(csrf_exempt, name='dispatch')
class QuizSubmitView(View):
    def post(self, request):
        data = json.loads(request.POST['data'])
        for ideograph_id, score in zip(data['ideographs'], data['scores']):
            proficiency = Proficiency.objects.filter(user=self.request.user).filter(ideograph_id=ideograph_id).first()
            if proficiency:
                if score == 1:
                    proficiency.score = min(100, proficiency.score + 10)
                else:
                    proficiency.score = max(0, proficiency.score - 10)
                proficiency.save()
            elif score == 1:
                Proficiency.objects.create(user=self.request.user, ideograph_id=ideograph_id, score=10)

        return HttpResponse()


class HelpView(TemplateView):
    template_name = "help.html"
