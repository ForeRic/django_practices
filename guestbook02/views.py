# url mapping # orm 방식
from django.http import HttpResponseRedirect
from django.shortcuts import render
from guestbook02.models import Guestbook


def index(request):
    results = Guestbook.objects.all().order_by('-regdate')
    data ={'guestbook_list': results}
    return render(request, 'guestbook02/index.html', data)

def add(request):
    guestbook = Guestbook()

    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']

    guestbook.save()

    return HttpResponseRedirect('/guestbook02')

def deleteform(request):
    return render(request, 'guestbook02/deleteform.html')

def delete(request):
    # id = request.POST["id"]
    # password = request.POST["password"]

    # guestbookmodel.deleteby_no_and_password(no, password)
    print("--" + request.POST['id'] + "--")
    #guestbook = Guestbook.objects.filter(id=request.GET['id']).filter(password=request.GET['password'])
    # 영속화 되어있는 객체를 뽑아와서 그걸 delete
    #guestbook.delete()
    return HttpResponseRedirect("/guestbook02")