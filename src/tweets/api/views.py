from rest_framework import generics
from django.db.models import Q
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import Tweet
from .serializers import TweetModelSerializer
from .pagination import StandardResultsPagination


class LikeTweetAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, format=None):
        message = "Not allowed"
        tweet_qs = Tweet.objects.filter(pk=pk)
        if request.user.is_authenticated():
            liked = Tweet.objects.tweet_toggle(request.user, tweet_qs.first())
            return Response({"liked": liked})
        return Response({"message": message}, status=400)


class RetweetAPIView(APIView):
    message = "Not allowed "
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, format=None):
        tweet_qs = Tweet.objects.filter(pk=pk)
        if tweet_qs.exists() and tweet_qs.count() == 1:
            if request.user.is_authenticated():
                new_tweet = Tweet.objects.retweet(request.user,
                                                  tweet_qs.first())
                if new_tweet is not None:
                    data = TweetModelSerializer(new_tweet).data
                    return Response(data)
                message = "cannot retweet the same in one day "
        return Response({"message": message}, status=400)


class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TweetDetailAPIView(generics.ListAPIView):
    pagination_class = StandardResultsPagination
    queryset = Tweet.objects.all()
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self, *args, **kwargs):
        tweet_id = self.kwargs.get("pk")
        qs = Tweet.objects.filter(pk=tweet_id)
        if qs.exists() and qs.count() ==1:
            parent_obj = qs.first()
            qs1 = parent_obj.get_children()
            qs = (qs | qs1).distinct().extra(select={"parent_id_null": 'parent_id IS NULL'})
            
        return qs.order_by("-parent_id_null", "-timestamp")
        
class SearchTweetAPIView(generics.ListAPIView):
    queryset = Tweet.objects.all().order_by("-timestamp")
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination
    
    def get_serializer_context(self, *args, **kwargs):
        context =super(SearchTweetAPIView, self).get_serializer_context(*args, **kwargs)
        context['request'] = self.request
        return context
    
    def get_queryset(self, *args, **kwargs):
        qs = self.queryset
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs  
    
        
class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination
    
    def get_serializer_context(self, *args, **kwargs):
        context =super(TweetListAPIView, self).get_serializer_context(*args, **kwargs)
        context['request'] = self.request
        return context

    def get_queryset(self, *args, **kwargs):
        requested_user = self.kwargs.get("username")
        if requested_user: 
            qs = Tweet.objects.filter(user__username=requested_user).order_by("-timestamp")
        else:
            my_following = self.request.user.profile.get_following()
            qs1 = Tweet.objects.filter(user__in=my_following)
            qs2 = Tweet.objects.filter(user=self.request.user)
            qs = (qs1 | qs2).order_by("-timestamp")
            print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs  
