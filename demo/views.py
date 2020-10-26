from django.shortcuts import render,HttpResponseRedirect
from hello import print_hello
from .forms import userChoiceForm

# Create your views here.


def home(request):
    context={
            "context":print_hello()
            }
    return render(request,"home.html",context)


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = userChoiceForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print("in here")
            return render(request,"thanks.html",{"Name":form.cleaned_data['your_name'],"your_choice":form.cleaned_data['choice1']})

    else:
        form = userChoiceForm()

    return render(request, 'form.html', {'form': form})


def thanks(request):
    pass
    