from telnetlib import STATUS
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.core.serializers import serialize
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

from .models import Note

# Create your views here.
def home(request):

    return render(request,'home.html',{})


def get_data(request):
    
    if request.user.is_authenticated:
        notes= Note.objects.filter(owner= request.user)
        geo_json=serialize('geojson', notes, geometry_field='location',
            fields=('title', 'description' , 'owner'))
        
        return HttpResponse(geo_json , content_type='text/json')
    else:
        return HttpResponse("Access Denied. Eror403", content_type='text/json')



def logout_view(request):
    logout(request)
    return redirect('home') 


def login_view(request):

    username = request.POST['username']
    passwd = request.POST['password']
    user = authenticate(request, username=username, password=passwd)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('home')
    