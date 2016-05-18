from django.shortcuts import render

def index(request):
        return render(request, 'mySite/index.html')

def loggedin(request):
        return render(request, 'registration/loggedin.html')

