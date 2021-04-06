from django.db import models


class Guestbook(models.Model):
    name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    message = models.CharField(max_length=4000) # Textfield 도 있음. 나중에 써보셈.
    regdate = models.DateTimeField(auto_now=True) #input_formats = ['%Y-%m-%d %p %h:%m:%s']

    def __str__(self): # 화면에 객체를 출력할 수 있게 string 으로 만드는 녀석.
        return f'Guestbook({self.name},{self.password},{self.message},{self.regdate})'