from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.

class IndexHandler(View):
    def get(self, request, *args, **kwargs):

        return HttpResponse("你好")