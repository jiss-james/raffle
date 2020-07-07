from .models import *
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        competitions = []
        for e in Competition.objects.all():
            competitions.append({"id": e.comp_id, "name": e.comp_name, "description": e.description, "fee": e.entry_fee, "prize": e.prize, "sdate": e.start_date, "edate":e.end_date})
            
        print(request.user)
        return render(request, 'index.html', {"competitions": competitions})
    else:
        return HttpResponseRedirect('/login')


def logged_in(request, user):
    competitions = []
    for e in Competition.objects.all():
        competitions.append({"id": e.comp_id, "name": e.comp_name, "description": e.description, "fee": e.entry_fee, "prize": e.prize, "sdate": e.start_date, "edate":e.end_date})

    return render(request, 'index.html', {"competitions": competitions})


def new_comp(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CompForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save(commit=True)
            return HttpResponseRedirect('/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = CompForm()
    return render(request, 'new_comp.html',  {'form': form})


def edit_comp(request, id):
    # handling case where Competition doesnt exist
    instance = get_object_or_404(Competition, comp_id=id)
    form = CompForm(instance=instance)
    if request.method == "POST":
        form = CompForm(request.POST, instance=instance)
        # saving an edited competition
        if 'save-btn' in request.POST:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        # deleting an existing competition 
        elif 'delete-btn' in request.POST:
            Competition.objects.filter(pk=id).delete()
            return HttpResponseRedirect('/')
    return render(request, 'edit_comp.html', {'form': form})


def enter_comp(request, id):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EntryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save(commit=True)
            return HttpResponseRedirect('/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = EntryForm()
    return render(request, 'enter_comp.html', {'form': form})

def signup(response):
    if response.method == "POST":
        form = SignupForm(response.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
	    form = SignupForm()

    return render(response, "signup.html", {"form":form})
