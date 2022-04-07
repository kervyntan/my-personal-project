from django.shortcuts import render

# Create your views here.
def home_view (request):
    return render(request, 'kervyn/index.html')

def about_view (request):
    return

def journey_view (request):
    return
