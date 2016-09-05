from django.shortcuts import render
from .management import config as cfg
from django.http import JsonResponse
import json

# Create your views here.

def index(request):
    context = {
    }
    return render(request, 'country_floral_app/index.html', context)

def order(request):
    keyword_list = []
    for x in cfg.CONFIG.KEYWORDS.values():
        keyword_list+=x
    context = {
        "keyword_list":cfg.CONFIG.KEYWORDS,
    }
    return render(request, 'country_floral_app/order.html', context)

def process(request):
    params = request.GET
    print("testsdfasdfasdfasdf")
    print(request)
    context ={}
    return JsonResponse(json.loads(json.dumps(context)))


def about(request):
    context = {
    }
    return render(request, 'country_floral_app/about.html', context)

def gallery(request):
    context = {
    }
    return render(request, 'country_floral_app/gallery.html', context)