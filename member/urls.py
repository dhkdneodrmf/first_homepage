from django.urls import path
from . import views

urlpatterns = [
    path('ok', views.hello ),
    path('ok1', views.main ),
    path('receive', views.rec ),
    path('send',views.send ),
    path('join', views.join),
    path('join2', views.join2),
    path('jcomp', views.jcomp),
    path('jcomp2', views.jcomp2),
    path('login', views.login),
    path('logined', views.logined),
    path('loginedcheck', views.check_logined),
    path('logout', views.logout),
    path('select', views.sel),
    path('intro/<str:colleage>/<str:major>/<int:age>/<str:detail>',views.intro),
    path('novel/',views.novel),
    path('novel/<int:chapter>/',views.novel),
    path('novel/<int:chapter>/<str:player1>/',views.novel),
    path('novel/<int:chapter>/<str:player1>/<str:player2>',views.novel),
    path('statictest',views.static),
    path('modpasswd',views.modpass),
    path('mpasswordcomp',views.modpass2), 
    path('withdrawal',views.exitmember),
    path('withdrawalcomp',views.exitmember2),
    path('ajax', views.ajax),
    path('ajax_test',views.ajaxrender),
    path('fileupload',views.upload_file),
    path('fileupload2',views.upload_file2),
    path('checkbox',views.checktest),
#    path('checkbox2',views.checktest2),
]

# <>는 주소로 뭔가 입력받을 수 있음.