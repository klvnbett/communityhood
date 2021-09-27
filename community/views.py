from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *


from decouple import config,Csv
import datetime as dt
from django.http import JsonResponse
import json
from django.db.models import Q
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return HttpResponse(request,'hood/index.html')

def blog(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    blogposts = BlogPost.objects.filter(neighbourhood=profile.neighbourhood)
    return render(request,'hood/blog.html',{"blogposts":blogposts})


def notification(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    all_notifications = notifications.objects.filter(neighbourhood=profile.neighbourhood)
    

    return render(request,'hood/notifications.html',{"notifications":all_notifications})