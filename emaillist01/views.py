from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from emaillist01 import models

def index(request):
    results = models.findall()    # templates 로 보내줘야
    data = {"emaillist_list": results}
    # templates 은 emaillist_list 로 보냄. 이름 참조. 맘대로 지어도 됨) 객체하나 필요. 이름을 하나 달아주면 됨.
    return render(request, 'emaillist01/index.html', data)

def form(request):
    return render(request, 'emaillist01/form.html')

def add(request): # redirect
    firstname = request.POST["fn"] # 이름을 받아오는 작업.
    lastname = request.POST["ln"]
    email = request.POST["email"]

    # print(firstname, lastname, email)
    models.insert(firstname, lastname, email)

    # return HttpResponse("<h1>Successfully assigned</h1>", content_type="text/html; charset=utf-8")
    # 쓰려면 HttpResponse import!
    return HttpResponseRedirect("/emaillist01")