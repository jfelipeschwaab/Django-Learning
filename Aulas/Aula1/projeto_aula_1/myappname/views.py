from django.shortcuts import render
from django.template import loader

# Create your views here.
def home(request):
    template = loader.get_template("app/home.html")
    return render(request, template)


def profile(request):
    pass