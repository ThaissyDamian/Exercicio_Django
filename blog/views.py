from django.views import View
from django.http import HttpResponse


class PostView(View):
    def get(self, request):
        return HttpResponse("Hello World")