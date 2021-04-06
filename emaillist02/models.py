from django.db import models

# primary key : id 로 자동으로 만들어 주기떄문에 붙일 필요가 없음.
class Emaillist(models.Model):
    # Model 에 상속받아서 save 라는 구현이 여기에 되어있음. 내부는 orm 이 알아서 하니까 신겨 ㄴㄴ.
    first_name = models.CharField(max_length=45) # table 칼럼 정하는 일
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=200)

    def __str__(self):
        return f'Emaillist({self.first_name}, {self.last_name}, {self.email})'
