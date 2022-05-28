import json

from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from System.models import *

#注册
@csrf_exempt
def register(request):  # 继承请求类
    print(request)
    if request.method == 'POST':  # 判断请求方式是否为 POST（此处要求为POST方式）
        username = request.POST.get('username')  # 获取请求体中的请求数据
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        if password_1 != password_2:  # 若两次输入的密码不同，则返回错误码errno和描述信息msg
            return JsonResponse({'errno': 1002, 'msg': "两次输入的密码不同"})
        else:
            # 新建 Author 对象，赋值用户名和密码并保存
            new_user = User(name=username, password=password_1)
            new_user.save()  # 一定要save才能保存到数据库中
            return JsonResponse({'errno': 0, 'msg': "注册成功"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

#登录
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username =  request.POST.get('username','')  # 获取请求数据
        password = request.POST.get('password','')
        user = User.objects.filter(name=username)
        if user.exists():
            author = User.objects.get(name=username)
            if author.password == password:  # 判断请求的密码是否与数据库存储的密码相同
                # 密码正确则将用户名存储于session（django用于存储登录信息的数据库位置）
                request.session['name'] = username
                return JsonResponse({'errno': 0, 'msg': "登录成功",'data':{'id':author.user_id,'username':username}})
            else:
                return JsonResponse({'errno': 1002, 'msg': "密码错误"})
        else:
            return JsonResponse({'errno': 1002, 'msg': "用户不存在"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

#上传书数据(管理员,先暂时用着)
@csrf_exempt
def savebook(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        image = request.POST.get('img','') # 封面图片
        author = request.POST.get('author','') # 封面图片
        press = request.POST.get('press','') # 封面图片  # 出版社
        introduction = request.POST.get('intro','') # 封面图片
        book = Book(name=name,image=image,author=author,press=press,introduction=introduction,score=0.0,heat=0)
        book.save()
        savebook = Book.objects.all().values('name','book_id')
        print(savebook)
        thisbook=Book.objects.get(name=request.POST.get('name',''))
        return JsonResponse({'errno': 0, 'msg': "存书成功",'data':{'id':thisbook.book_id}})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

#上传电影数据(管理员,先暂时用着)
@csrf_exempt
def savemovie(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        image = request.POST.get('img','') # 封面图片
        director = request.POST.get('director','') # 封面图片
        year = request.POST.get('year','')
        actor = request.POST.get('actor','')
        introduction = request.POST.get('intro','') # 封面图片
        movie=Movie(name=name,image=image,director=director,actor=actor,year=year,introduction=introduction,score=0.0,heat=0)
        movie.save()
        savemovie =Movie.objects.all().values('name','movie_id')
        print(savemovie)
        print('\n')
        thismovie=Movie.objects.get(name=request.POST.get('name',''))
        return JsonResponse({'errno': 0, 'msg': "存书成功",'data':{'id':thismovie.movie_id}})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

@csrf_exempt
def hotmovie(request):
    if request.method == 'POST':
        num = request.POST.get('num')
        movielist=Movie.objects.all().order_by('heat').all()
        hotmovielist=[]
        i=0
        while i<10:
            hotmovielist.append({
                'name':movielist[i].name,
                'image':movielist[i].image,
                'director':movielist[i].director,
                'id':movielist[i].movie_id
            })
            i=i+1
        return JsonResponse({'errno':0,'msg':'查询热门电影','data':hotmovielist})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
