from django.shortcuts import render
from django.views import View

# Create your views here.
from .models import Hashtag

class HashTagView(View):
    def get(self, request, hashtag, *args, **kwargs):
        obj, create = Hashtag.objects.get_or_create(tag=hashtag)
        return render(request, "tag_tweets.html", {"obj":obj})