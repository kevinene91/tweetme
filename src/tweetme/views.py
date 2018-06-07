from django.shortcuts import render
from django.views import View
from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model( ) 
def home(request):
    return render(request, "home.html", {})

class SearchView(View):
    
    def get(self, request, *args, **kwargs):
        q = request.GET.get("q")
        qs = None
        if q:
            qs = User.objects.filter(
                Q(username__icontains=q)
            )
        context = {"users": qs}
        return render(request, "search.html", context)