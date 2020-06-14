from .models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CompForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save(commit = True)
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = CompForm()
    return render(request, 'index.html',  {'form': form})
