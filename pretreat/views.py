from django.shortcuts import render
from django.http import HttpResponse
from .forms import AppinfoForm

# Create your views here.
def upload_apk(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AppinfoForm(request.POST,request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse('success')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AppinfoForm()

    return render(request, 'upload.html', {'form': form})