from django.db import models

# Create your models here.
from MySQLdb import connect, OperationalError
from MySQLdb.cursors import DictCursor


def findall():
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor(DictCursor)

        # sql 실행
        sql = '''
        select 	no, 
		        name, 
		        message, 
                date_format(reg_date, '%Y-%m-%d %p %h:%i:%s') as reg_date
        from 	guestbook 
        order by reg_date desc'''
        cursor.execute(sql)

        # 결과 받아오기
        results = cursor.fetchall()

        # 자원정리
        cursor.close()
        db.close()

        # 결과 반환
        return results

    except OperationalError as err:
        print(f'sorry. plz try later :{err}')


def insert(name, password, message):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor()

        # sql 실행
        sql = 'insert into guestbook values(null, %s, %s, %s, now())'
        count = cursor.execute(sql, (name, password, message))

        # commit
        db.commit()

        # 자원정리
        cursor.close()
        db.close()

        # 결과 반환
        return count == 1

    except OperationalError as err:
        print(f'sorry. plz try later :{err}')


def deleteby_no_and_password(no, password):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor()

        # sql 실행
        sql = 'delete from guestbook where no = %s and password = %s'
        count = cursor.execute(sql, (no, password))

        # commit
        db.commit()

        # 자원정리
        cursor.close()
        db.close()

        # 결과 반환
        return count == 1

    except OperationalError as err:
        print(f'sorry. plz try later :{err}')

def conn():
    return connect(
        user='webdb',
        password='webdb',
        host='localhost',
        port=3306,
        db='webdb',
        charset='utf8')