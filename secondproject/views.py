from django.shortcuts import render

def index(request):
    return render(
        request,
        'secondproject/index.html',
    )
def login_page(request):
    return render(
        request,
        'secondproject/login_page.html',
    )
def signup_page(request):
    return render(
        request,
        'secondproject/signup_page.html',
    )
def health_page(request):
    return render(
        request,
        'secondproject/health_page.html',
    )
# Create your views here.
