from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ApplicationForm

from django.shortcuts import render
from django.contrib import messages


def form_view(request):
    context = {}
   

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
     # create object of form
        form = ApplicationForm(request.POST or None, request.FILES or None)

        # check if form data is valid
        if form.is_valid():
            print("value ", form.cleaned_data['commence'])
        # save the form data to model

            form.save()
            messages.success(request, 'Form submission successful')

           

            return HttpResponseRedirect('/')

    else:
        form = ApplicationForm()

    context['form'] = form
    return render(request, "index.html", context)
