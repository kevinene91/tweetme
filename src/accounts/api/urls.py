
from django.conf.urls import url
from tweets.api.views import TweetListAPIView

urlpatterns = [
   
    url(r'^(?P<username>[\w.@+-]+)/tweet/$', TweetListAPIView.as_view(), name='list'),
    # url(r'^create/$', tweet_create_view, name='create')
]