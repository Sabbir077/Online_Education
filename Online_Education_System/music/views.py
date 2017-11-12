from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from .models import Album
# Create your views here.
def index(request,):

    all_album = Album.objects.all()
    return render(request,'music/index.html',{'all_album':all_album})


def song(request):
    return HttpResponse("song page")

def album(request):
    return HttpResponse("<h1>welcome to album page</h1>")


def detail(request,album_id):


     context = get_object_or_404(Album,pk=album_id)

     return render(request,'music/detail.html',{'context':context})


def sabbir(request):
    return HttpResponse("<h1> Hi Sabbir </h1>")
