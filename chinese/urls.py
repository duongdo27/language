from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^ideograph/(?P<pk>\d+)$', views.IdeographDetailView.as_view(), name='ideograph'),
]
