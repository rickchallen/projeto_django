from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def teste(request):
    return render(request,'Teste2.html')