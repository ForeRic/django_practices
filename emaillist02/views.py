from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from emaillist02.models import Emaillist


def index(request):
    results = Emaillist.objects.all().order_by('-id')
    data = {"emaillist_list": results}
    return render(request, 'emaillist02/index.html', data)

def form(request):
    return render(request, 'emaillist02/form.html')


def add(request): # redirect
    emaillist = Emaillist() # class 불러옴. 객체 지향은 java로. Lscript랑.. 그리고 나서 파이썬에서 객체지향을 하는것이..
    emaillist.firstname = request.POST["fn"] # 이름을 받아오는 작업.
    emaillist.lastname = request.POST["ln"]
    emaillist.email = request.POST["email"]

    return HttpResponseRedirect("/emaillist02")