
from django.conf.urls import url, include
from django. views.generic.base import RedirectView
from .views import (UserDetailView,
                    UserfollowView )



urlpatterns = [

    # url(r'^$', RedirectView.as_view(url="/")),
    # url(r'^search/$', TweetListView.as_view(), name='list'),
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),
    url(r'^(?P<username>[\w.@+-]+)/follow/$', UserfollowView.as_view(), name='follow'),

    # url(r'^create/$', TweetCreateView.as_view(), name='create'),
    # url(r'^(?P<pk>\d+)/edit/$', TweetViewUpdate.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/delete/$', TweetViewDelete.as_view(), name='delete'),

    # url(r'^create/$', tweet_create_view, name='create')
]