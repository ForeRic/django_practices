# Django Practices

## 장고 프로젝트 (django_practices) 만들기
### 1. pycharm 에서 프로젝트 (django_practices) 생성/설정/테스트

### 2. django libray 설치 (터미널에서) 
```python
(env) pip install django 
````
- 새로운 프로젝트를 만들 때마다 매번 설치해야 함.

### 3. mysqlclient library 설치 
```python
(env) pip install mysqlclient
```
### 4. 장고 프로젝트 생성 (django_practices라고 이름 지은)
```python
(env) django-admin startproject django_practices
```
- pycharm project/django_practices/django_practices  
- 파이참 프로젝트 밑에(사용자계정에서) / 
  프로젝트 만들면서 새롭게 만들어진 디렉토리(1) 밑에 / 
  다른 디렉토리(2)가 생성
  >pycharm project -- from 사용자 계정
  > >django_practices -- (1)
  > >>django_practices -- (2)

### 5. 디렉토리 정리(pycharm 프로젝트와 장고 프로젝트를 일치시켜 주기)

- manage.py 는 프로젝트 만들면서 생성된 디렉토리(1) 밑으로 옮겨주고,
그 외에 모든 파일은 다른 디렉토리(2)가 생성된 곳으로 한 단계씩 윗 디렉토리로 옮기기.
- 처음에 생성시엔, 디렉토리가 다음과 같이 생성됨.
  >django_practices(1)
  > >django_practices(2) -- 이곳에 manage.py 가 있고
  > >>django_practics -- 이곳에 그 외의 파일들이 있음. (없애야 할 디렉토리)
   
  그 외의 파일들: settings.py 와 urls.py를 주로 쓰게 됨.
  >__ init __.py  
  > asgi.py  
  > __settings.py__  
  > __urls.py__  
  > wsgi.py
### 6. 초기 설정(settings.py)
1) Time Zone 설정
```python
TIME_ZONE = 'Asia/Seoul'
```
2) database 설정 
- 초기엔 'ENGINE: django.db.backends.xxx' (뒤에 xxx 가 다른걸로 설정되어 있음)
- 'ENGINE': 'django.db.backends.mysql' (뒤를 mysql 로 바꿔줌. 우리는 mysql 설치해서 쓰니까)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webdb',
        'USER': 'webdb',
        'PASSWORD': 'webdb',
        'HOST': 'localhost',
        'PORT': 3306
    }
}
```
### 7. 장고 프로젝트의 관리 어플리케이션 (기본 설치)이 사용하는 DB 생성하기
```python
(env) python manage.py migrate
```
실행시,  
(venv) C:\Users\사용자계정\PycharmProjects\django_practices>python manage.py migrate  
Operations to perform:  
  Apply all migrations: admin, auth, contenttypes, sessions  
Running migrations:  
  Applying contenttypes.0001_initial... OK  
  Applying auth.0001_initial... OK  
  Applying admin.0001_initial... OK  
  Applying admin.0002_logentry_remove_auto_add... OK  
  Applying admin.0003_logentry_add_action_flag_choices... OK  
  Applying contenttypes.0002_remove_content_type_name... OK  
  Applying auth.0002_alter_permission_name_max_length... OK  
  Applying auth.0003_alter_user_email_max_length... OK  
  Applying auth.0004_alter_user_username_opts... OK  
  Applying auth.0005_alter_user_last_login_null... OK  
  Applying auth.0006_require_contenttypes_0002... OK  
  Applying auth.0007_alter_validators_add_error_messages... OK  
  Applying auth.0008_alter_user_username_max_length... OK  
  Applying auth.0009_alter_user_last_name_max_length... OK  
  Applying auth.0010_alter_group_name_max_length... OK  
  Applying auth.0011_update_proxy_permissions... OK  
  Applying auth.0012_alter_user_first_name_max_length... OK  
  Applying sessions.0001_initial... OK

- mysql 5.1x 인 경우 오류 발생시, manage.py 에 다음 코드를 추가하고 다시 실행
```python
from django.db.backends.mysql.base import DatabaseWrapper
DatabaseWrapper.data_types['DateTimeField'] = 'datetime'
```
### 8. 프로젝트(사이트) 관리 계정 만들기
```python
(env) python manage.py createsuperuser
```
실행시,  
Username (leave blank to use 'bit_r39'): admin  
Email address: 자기 이메일  
Password: 8자 이상이 좋음. 자기가 생성. 그러나 보이지 않음 터미널에서 실행시에  
Password (again): 같은 비번 칠 것  
Superuser created successfully.

### 9. 지금까지 작업 내용 확인
1) 서버 시작하기 (localhost:9999  할때 필요한 포트 열기)
- 9999: 포트를 여는 작업
```python
(env) python manage.py runserver 0.0.0.0:9999
```

2) 브라우저로 접근하기
- url http://localhost:9999 로 접근
- 이렇게 하는 이유는: db 생성시 localhost 로 만들었고, 9999는 포트 넘버라서
-----------------------------------

## 2. 프로젝트 (django_practices)에 application 추가하기

#### 1. Application 들의 통합 template 디렉토리 templates 만들기
1) 디렉토리 생성  
django_practices (프로젝트 처음 만들때 만들어진 디렉토리(1))
> django_practices  -- (1)
>> templates -- (django_practices(2) 과 같은 위치)
   
2) template 디렉토리 설정 (setting.py)
- TEMPLATES 안에 있는 directory (경로) 설정해주는 작업. url이 받아서 읽어올 곳. (url:http://localhost:9999)
```python
import os

   'DIRS': [os.path.join(BASE_DIR,'templates')]
```
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
####2. helloworld Application 만들기
1) Application 생성
```shell
(venv) # python manage.py startapp helloworld
```
- 현재 돌아가는 서브 종료: ctrl + C
2) Application 등록 (setting.py) :  'helloworld' 등록해주는 작업
```python
INSTALLED_APPS = [
    'helloworld',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
3) Application의 templates 디렉토리 생성  
>django_practices  -- (1)
>>templates   --(2와 같은 위치)
>>>helloworld
   
4) urls.py 에 URL 등록하고 views.py 에 요청 처리 함수 만들고 template(html) 연결하고.....(반복반복)

----------
<
오늘 총 작업하면서 열어봤던 파일들> 
- settings.py  
-  urls.py  
- views.py
- tags.html  
  (마지막에 만든 helloworld 디렉토리 안에 있는 html 파일로, 
  웹에서 localhost:9999/tags 주면 화면에 출력할 내용을 입력하는 곳)
  
- hello2.html   
  (tags.html 과 같이 pycharm 에서 helloworld 밑에 html 파일을 만든 것임)