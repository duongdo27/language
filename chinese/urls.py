from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^ideograph/(?P<pk>\d+)$', views.IdeographDetailView.as_view(), name='ideograph'),
    url(r'^deck_list$', views.DeckListView.as_view(), name='deck_list'),
    url(r'^deck/(?P<pk>\d+)$', views.DeckDetailView.as_view(), name='deck'),
    url(r'^lesson_quiz/(?P<deck_id>\d+)/(?P<lesson>\d+)$', views.QuizView.as_view(), name='lesson_quiz'),
    url(r'^deck_quiz/(?P<deck_id>\d+)$', views.QuizView.as_view(), name='deck_quiz'),
    url(r'^quiz_submit', views.QuizSubmitView.as_view(), name='quiz_submit'),
]
