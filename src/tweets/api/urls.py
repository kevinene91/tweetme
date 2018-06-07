
from django.conf.urls import url
# from django. views.generic.base import RedirectView
from .views import (
                    TweetListAPIView,
                    TweetCreateAPIView,
                    RetweetAPIView,
                    LikeTweetAPIView,
                    TweetDetailAPIView,
    )




urlpatterns = [
    # url(r'^$', RedirectView.as_view(url="/")),
    url(r'^$', TweetListAPIView.as_view(), name='list'),
    
    url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name='retweet'),
    url(r'^(?P<pk>\d+)/like/$', LikeTweetAPIView.as_view(), name='like'),
    url(r'^(?P<pk>\d+)/$', TweetDetailAPIView.as_view(), name='detail'),
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'),
    # url(r'^(?P<pk>\d+)/edit/$', TweetViewUpdate.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/delete/$', TweetViewDelete.as_view(), name='delete'),

    # url(r'^create/$', tweet_create_view, name='create')
]