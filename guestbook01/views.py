from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from guestbook01 import models


def index(request):
    results = models.findall()
    data = {"guestbooks": results}
    return render(request, 'guestbook01/index.html', data)

def add(request):
    name = request.POST["name"] # 이름을 받아오는 작업.
    password = request.POST["password"]
    message = request.POST["message"]

    # print(no, password, message)
    models.insert(name, password, message)

    # return HttpResponse("<h1>Successfully assigned</h1>", content_type="text/html; charset=utf-8")
    # 쓰려면 HttpResponse import!
    return HttpResponseRedirect("/guestbook01")

def deleteform(request):

      return render(request, 'guestbook01/deleteform.html')

def delete(request):
    no = request.POST["no"]
    password = request.POST["password"]

    models.deleteby_no_and_password(no, password)

    return HttpResponseRedirect("/guestbook01")

