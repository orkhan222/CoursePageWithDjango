from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from .models import About, Basic, Fall, Image, Make, Our, Related, Slider,Apply,Featured, Store, Teacher,Basic,Related
# Create your views here.
from django.forms import forms


def index(request):
    slider= Slider.objects.all()
    about = About.objects.all()
    apply= Apply.objects.all()
    fall= Fall.objects.all()
    featured= Featured.objects.all()
    teacher= Teacher.objects.all()
    image= Image.objects.all()
    store= Store.objects.all()
    context={
        'slider':slider,
        'about':about,
        'apply':apply,
        'fall':fall,
        'featured':featured,
        'teacher':teacher,
        'image':image,
        'store':store
    }
    return render(request, 'index.html',context)


def courses(request):
    our=Our.objects.all()

    context={
        'our':our,
    }
    return render(request, 'courses.html',context)


def coursessingle(request):
    basic= Basic.objects.all()
    make=Make.objects.all()
    related=Related.objects.all()

    context={
        'basic':basic,
        'make':make,
        'related':related
    }
    return render(request, 'courses-single.html',context)


def register(request):
    
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')