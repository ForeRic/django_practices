from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
import guestbook01.models as guestbookmodel


def index(request):
    results = guestbookmodel.findall()
    data = {"guestbook_list": results}
    return render(request, 'guestbook01/index.html', data)

def add(request):
    name = request.POST["name"] # 이름을 받아오는 작업.
    password = request.POST["password"]
    message = request.POST["message"]

    # print(no, password, message)
    guestbookmodel.insert(name, password, message)

    # return HttpResponse("<h1>Successfully assigned</h1>", content_type="text/html; charset=utf-8")
    # 쓰려면 HttpResponse import!
    return HttpResponseRedirect("/guestbook01")

def deleteform(request):
    # no = request.GET["no"]
    # data = {"no": no }
    # return render(request, 'guestbook01/deleteform.html', data)
    # 이렇게 쓰면 deleteform 가서 value = {{ no }} 로 바꿔주면 됨. 데이터를 받아서 넣어주니까.

    return render(request, 'guestbook01/deleteform.html')
    # 이렇게만 쓸 때는 deleteform 가서 value = {{ request.GET.no }}

def delete(request):
    no = request.POST["no"]
    password = request.POST["password"]

    guestbookmodel.deleteby_no_and_password(no, password)

    return HttpResponseRedirect("/guestbook01")

