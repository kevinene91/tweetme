
from django.conf.urls import url
from django. views.generic.base import RedirectView
from .views import (RetweetView,
                    tweet_detail_view,
                    TweetCreateView,
                    TweetViewUpdate,
                    TweetViewDelete,
                    TweetListView)


urlpatterns = [
    url(r'^$', RedirectView.as_view(url="/")),
    url(r'^search/$', TweetListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', tweet_detail_view, name='detail'),
    url(r'^(?P<pk>\d+)/like/$', RetweetView.as_view(), name='retweet'),
    url(r'^create/$', TweetCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/edit/$', TweetViewUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', TweetViewDelete.as_view(), name='delete'),
    # url(r'^create/$', tweet_create_view, name='create')
]