from django.db import models
from django.db.models.fields import EmailField
from ckeditor.fields import RichTextField
    #ORM의 역할: SQL을 직접 작성하지 않아도 데이터베이스로 접근해 CRUD(조회/추가/수정/삭제) 가 가능하게 해준다.

class User(models.Model):
    userid=models.CharField(max_length=64, verbose_name='아이디')
    # CHarField는 문자열 필드
    #max_length 최대 길이, 길이 제한
    username=models.CharField(max_length=64, verbose_name='사용자명')
    password=models.CharField(max_length=64, verbose_name='비밀번호' , default='')
    email=models.EmailField(max_length=128, verbose_name='이메일' , null=True)
    introduce=models.TextField(max_length=6000,verbose_name='자기소개' , null=True)
    registered=models.DateTimeField(auto_now_add=True, verbose_name='등록')
    #DateTmeField  auto_now_add=True
    #0000-00-00 00:00:00 datetime
    GENDERS =(('M','남성(Man)'),('W','여성(woman)'))
    gender=models.CharField(max_length=1, verbose_name='성별', choices=GENDERS)
    #enum('M', 'W')
    #남성 여성은 별칭


    #TextField
    #IntergerField
    #null=True(기본값은 False)
    #default=
    body = RichTextField()