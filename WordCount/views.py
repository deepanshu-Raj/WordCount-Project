# views.py is a module that returns a https response
#
from django.http import HttpResponse
from django.shortcuts import render
import operator

#Http response must be returned from this module
def home(request):
    return render(request,'home.html')

def Count(request):
    fulltext = request.GET['fulltext']
    list = fulltext.split()

    dict = {}
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    lst = sorted(dict.items(),key = operator.itemgetter(1),reverse = True)
    return render(request,'count.html',{'words':lst,'count':len(dict),'totalWords':len(list)})

def AboutUs(request):
    return render(request,'aboutus.html')

def Subscribe(request):
    return render(request,'subscribe.html')
