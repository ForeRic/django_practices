from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'helloworld/main.html')

def hello1(request):
    name = request.GET['name']
    return HttpResponse(f'<h1>Hello {name} </h1><a href="/"> 메인으로가기', content_type='text/html; charset = utf-8')



def tags(request):
    return render(request, 'helloworld/tags.html')

def form(request):
    return render(request, 'helloworld/form.html')

def join(request):
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']
    hobbies = request.POST.getlist("hobbies")
    description = request.POST["desc"]

    print(email, password, gender, hobbies, description)
    return HttpResponse('Congrats! You are welcome on board!', content_type='text/plain; charset = utf-8')