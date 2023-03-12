from django.shortcuts import render

def index(request):
    return render(
        request,
        'secondproject/index.html',
    )
# Create your views here.
