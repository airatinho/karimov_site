from django.shortcuts import render
# Create your views here.

def index(request):
    data={'title': 'Главная мявочная',
          'values':['1','hello','мявочка'],
          'obj':{'car':'bmw',
                 'type':'sportcar',
                 'host':'ayrat'
                 }
          }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')