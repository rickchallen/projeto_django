from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Blog/home.html')

def noticias(request):
    return render(request,'noticias/noticias.html')
