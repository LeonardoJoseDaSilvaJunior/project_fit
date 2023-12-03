from django.shortcuts import render

def home(request):
    return render (request , 'index.html')

def LoginPage(request):
    return render(request, 'signin.html')

def SignOutPage(request):
    pass

def SignUpPage(request):
    return render(request, 'signup.html')