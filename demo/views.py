from django.shortcuts import render
from hello import print_hello
# Create your views here.
def home(request):
    context={
            "context":print_hello()
            }
    return render(request,"home.html",context)
