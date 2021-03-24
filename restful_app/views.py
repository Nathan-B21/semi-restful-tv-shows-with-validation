from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show
def index(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request,"index.html", context)

def newshow_page(request):
    
    return render(request,"newshow.html")

def addshow(request):
    errors = Show.objects.showValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/newshow_page') # PROBABLY WRONG    
    else:
        newshow = Show.objects.create(title = request.POST['title'], network = request.POST['network'], release_date = request.POST['releasedate'], desc = request.POST['desc'])
    return redirect(f'/showinfo/{newshow.id}')

def showinfo(request, showId):
    context = {
        'show' : Show.objects.get(id = showId)
    }
    return render(request, 'showinfo.html', context)
def display_editshow(request, showId):
    context = {
        'show': Show.objects.get(id = showId)
    }
    return render(request, 'showedit.html', context)


def editshow(request, showId):
    errors = Show.objects.showValidator(request.POST)
    showObject = Show.objects.get(id = showId)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/showedit/{showObject.id}') # Probably wrong
    else:
        showObject = Show.objects.get(id = showId)
        showObject.title = request.POST['title']
        showObject.network = request.POST['network']
        showObject.release_date = request.POST['releasedate']
        showObject.desc = request.POST['desc']
        showObject.save()
    return redirect(f'/showinfo/{showObject.id}')
    
def deleteshow(request, showId):
    showObject = Show.objects.get(id = showId)
    showObject.delete()
    return redirect("/")
