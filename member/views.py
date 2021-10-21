from django.shortcuts import render
import random
from .models import User
# from django.http import HttpResponseRedirect
from django.shortcuts import render
# from .forms import UploadFileForm
import os
import torch
# Imaginary function to handle an uploaded file.

# def upload(req):
#     return render(req, 'fileuploadtest.html')

# def upload_file(req):
#     if req.method == 'POST':
#         form = UploadFileForm(req.POST, req.FILES)
#         if form.is_valid():
#             handle_uploaded_file(req.FILES['file'])
#             return render(req, "uploadsucces.html")
#     else:
#         form = UploadFileForm()
#     return render(req, 'upload.html', {'form': form})

def upload_file(req):
    if req.method == 'POST':
        # print(req.FILES['my_files'])
        with open( os.path.abspath('./member/static/'+ req.FILES['my_files'].name ), 'wb+') as destination:
            for chunk in req.FILES['my_files'].chunks():
                destination.write(chunk)
        return render(req, "uploadsucces.html")
    else:
        return render(req, 'upload.html')

def upload_file2(req):
    if req.method == 'POST':
        with open( os.path.abspath('./member/static/user/'+ req.FILES['uploadfiles'].name ), 'wb+') as destination:
            for chunk in req.FILES['uploadfiles'].chunks():
                destination.write(chunk)
        return render(req, "uploadsucces.html",{'filename':req.FILES['uploadfiles'],'filecotent':destination})
    else:
        return render(req, 'upload2.html')


# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

# Create your views here

def hello(req) :
    c=random.randint(1,10)
    if c>5:
        d="상류층"
    else:
        d="하류층"
    return render(req,'a.html',{'parameter1':c, 'parameter2':d})

def main(req) :
    return render(req,'index.html')

def rec(req):
    return render(req, 'd.html',{'param1':req.POST.get('my_info')})

def send(req):
    return render(req, 'c.html')

def join(req):
    return render(req, 'join.html')

def jcomp(req):
    # 일단 넘어온 KR을 db에 넣는 코드 삽입
    if req.POST.get('jnational') =="한국":
        nation="한국"
    return render(req, 'joincomplete.html',{'jid':req.POST.get('jid'),'jpassword':req.POST.get('jpassword'),'jname':req.POST.get('jname'),'jcellphone1':req.POST.get('jcellphone1'),'jcellphone2':req.POST.get('jcellphone2'),'jcellphone3':req.POST.get('jcellphone3'),'jemail':req.POST.get('jemail'),'jnational':nation,'jzip':req.POST.get('jzip'),'jcity':req.POST.get('jcity'),'jcounty':req.POST.get('jcounty'),'jremainadd':req.POST.get('jremainadd'),'jgame':req.POST.get('jgame'),'jintro':req.POST.get('jintro')})

def sel(req):
    return render(req, 'e.html')

def intro(req, colleage, major, age, detail):
    return render(req, 'g.html', {'c':colleage, 'm':major,'a':age, 'd':detail})

def novel(req, chapter=1, player1="조영래", player2="여자친구"):
    return render(req, 'f.html', {'c':chapter, 'p1':player1,'p2':player2})

def static(req):
    return render(req, 'h.html')

def join2(req):
    return render(req, 'join2.html')

def jcomp2(req):
    new_member=User(userid=req.POST.get('jid'),username=req.POST.get('jname'),password=req.POST.get('jpassword'),email=req.POST.get('jemail'),introduce=req.POST.get('jintro'),gender=req.POST.get('jgender'))
    new_member.save()
    return render(req, 'joincomplete2.html')

def login(req):
    if req.session.get('userid'):
        return render(req, 'logged_succes2.html',{'id':req.session.get('userid'),'re':'re'})
    else:
        return render(req, 'login.html')

def logined(req):
    log_member=User.objects.filter(userid=req.POST.get('eid'),password=req.POST.get('epassword'))
    #print(log_member)
    if log_member:
        req.session['userid']=req.POST.get('eid')
        return render(req, 'logged_succes.html',{'sucess_mem':log_member})
    else:
        return render(req, 'logged_fail.html')

def check_logined(req):
    if req.session.get('userid'):
        return render(req, 'logged_succes2.html',{'id':req.session.get('userid')})
    else:
        return render(req, 'login.html',{'sucess_msg':'로그인 먼저 해주세요.'})

def logout(req):
    if req.session.get('userid'):
        req.session.pop('userid')
        return render(req, 'login.html',{'sucess_msg':'안전하게 로그아웃되었습니다.'})
    else:
        return render(req, 'login.html',{'sucess_msg':'로그아웃할 회원이 없습니다. 올바르지 않은 접근입니다.'})

def modpass(req):
    return render(req, 'mpassword.html')

def modpass2(req):
    try:
        modpassuser=User.objects.get(userid=req.POST.get('mid'))
        modpassuser.password = req.POST.get('mpassword')
        modpassuser.save()
        return render(req, 'login.html',{'sucess_msg':'비밀번호 변경이 정상적으로 완료되었습니다. 변경한 비밀번호로 로그인하세요.'})
    except User.DoesNotExist:
        return render(req, 'mpassword.html',{'err':'변경하려는 아이디를 찾을 수 없습니다.(아이디를 다시 입력하세요.)'})

def exitmember(req):
    return render(req, 'exitmember.html',{'inputid':req.POST.get('exitid')})

def exitmember2(req):
    try:
        exituser=User.objects.get(userid=req.POST.get('exitid'),password=req.POST.get('exitpassword'))
        exituser.delete()
        return render(req, 'login.html',{'sucess_msg':'회원탈퇴가 완료되었습니다. 언젠가 다시 만날 그날을 기다리며...'})
    except User.DoesNotExist:
        return render(req, 'exitmember.html',{'err':'아이디 혹은 비밀번호가 잘못입력되어 회원탈퇴가 완료되지 않았습니다. 다시 시도해주세요.','inputid':req.POST.get('exitid')})

def ajax(req):
    return render(req, 'ajaxtest.html')

def ajaxrender(req):
    try:
        fuser=User.objects.get(userid=req.POST.get('id'),password=req.POST.get('pw'))
        return render(req, 'b.html', {'parameter1':fuser.userid, 'parameter2':fuser.password, 'parameter3':fuser.username,'parameter4':fuser.registered,'parameter5':fuser.get_gender_display} )
    except User.DoesNotExist:
        return render(req, 'b.html',{'err':'아이디 혹은 비밀번호가 잘못입력되었습니다. 다시 시도해주세요.'})

def checktest(req):
#    return render(req, 'i.html')
    if req.POST.getlist('hobby'):
        return render(req, 'i.html',{'objects':req.POST.getlist('hobby')})
    else:
        return render(req, 'i.html')

# def checktest2(req):
#    return render(req, 'j.html',{'objects':req.POST.getlist('hobby')})

def trafaccident(req):
    return render(req, 'accident.html')

def toeic_ai(req):
    if req.method == 'POST':
        x_train = torch.FloatTensor([[int(req.POST.get('day1'))],[int(req.POST.get('day2'))],[int(req.POST.get('day3'))]])
        y_train = torch.FloatTensor([[int(req.POST.get('score1'))],[int(req.POST.get('score2'))],[int(req.POST.get('score3'))]])
        W = torch.zeros(1)
        b = torch.zeros(1)

        lr = 0.00025

        epochs = 200000

        len_x = len(x_train)

        for epoch in range(epochs):
          hypothesis = x_train * W + b
          cost = torch.mean((hypothesis -y_train)**2)

          gradient_w = torch.sum((W*x_train - y_train +b)*x_train)/ len_x
          gradient_b = torch.sum((W*x_train - y_train +b))/len_x

          W -= lr * gradient_w
          b -= lr * gradient_b
        if epoch % 10000 == 0:
            print('Epoch {:4d}/{} W:{:.6f} b:{:.6f} Cost: {:.6f}'.format(epoch,epochs,W.item() ,b.item() , cost.item()))
        return render( req, 'toeic_output.html', { 'W':W.item(), 'b':b.item() } )
    else:
        return render(req, 'toeic_input.html')