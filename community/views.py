from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *



import datetime as dt
from django.http import JsonResponse
import json
from django.db.models import Q
from django.contrib.auth.models import User


# Create your views here.
def index(request):

    return render(request,'hood/index.html')

def notification(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    all_notifications = notifications.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request,'hood/notifications.html',{"notifications":all_notifications})

def blog(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    blogposts = BlogPost.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request,'hood/blog.html',{"blogposts":blogposts})

def health(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    healthservices = Health.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request,'hood/health.html',{"healthservices":healthservices})

def authorities(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    authorities = Authorities.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request,'hood/authorities.html',{"authorities":authorities})

def businesses(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    businesses = Business.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request,'hood/businesses.html',{"businesses":businesses})

def view_blog(request,id):
    blog = BlogPost.objects.get(id=id)

    return render(request,'hood/view_blog.html',{"blog":blog})

def user_profile(request,username):
    user = User.objects.get(username=username)
    profile =Profile.objects.get(username=user)

    return render(request,'hood/user_profile.html',{"profile":profile})