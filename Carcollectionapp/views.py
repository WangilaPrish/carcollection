from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def mustang(request):
    return render(request, 'mustang.html')
# Create your views here.
def ferrari(request):
    return render(request, '1957ferrari.html')
def chevrolet(request):
    return render(request, '1963chevrolet.html')
def porsche(request):
    return render(request, '1973porsche.html')
def camaro(request):
    return render(request, 'camaro.html')