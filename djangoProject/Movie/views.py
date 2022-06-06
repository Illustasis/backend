from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from System.models import *
import json
# Create your views here.
@csrf_exempt
def hot(request):
    if request.method == 'POST':
        num = request.POST.get('num')
        movielist=Movie.objects.all().order_by('heat').all()
        hotmovielist=[]
        i=0
        while i<int(num):
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

@csrf_exempt
def high(request):
    if request.method == 'POST':
        num = request.POST.get('num')
        movielist=Movie.objects.all().order_by('score').all()
        highmovielist=[]
        i=0
        while i<int(num):
            highmovielist.append({
                'name':movielist[i].name,
                'image':movielist[i].image,
                'director':movielist[i].director,
                'id':movielist[i].movie_id
            })
            i=i+1
        return JsonResponse({'errno':0,'msg':'查询热门电影','data':highmovielist})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

@csrf_exempt
def collect(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        movie_id = request.POST.get('movie_id')
        collect = Collect(resource_id=movie_id, column=2, user_id=user_id)
        collect.save()
        return JsonResponse({'errno':0, 'msg': "收藏成功"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

@csrf_exempt
def uncollect(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        movie_id = request.POST.get('movie_id')
        collection = Collect.objects.filter(resource_id=movie_id, column=2, user_id=user_id)
        if collection.exists() :
            collect=Collect.objects.get(resource_id=movie_id, column=2, user_id=user_id)
            collect.delete()
            return JsonResponse({'errno':0, 'msg': "已取消收藏"})
        else:
            return JsonResponse({'errno':200, 'msg': "取消收藏失败"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
@csrf_exempt
def collection(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        collections = Collect.objects.filter(user_id=user_id,column=2)
        print(collections)
        collect=[]
        for item in collections:
            movie = Movie.objects.get(movie_id=item.resource_id)
            collect.append({
                'id': movie.movie_id,
                'name':movie.name,
                'director':movie.director,
                'image':movie.image,
                'star':movie.score,
            })
        return JsonResponse({'errno':0, 'data':collect})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

@csrf_exempt
def detail(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')  # 获取图书ID
        user_id = request.POST.get('user_id')  # 获取用户ID
        movie = Movie.objects.get(movie_id=movie_id)
        users_id = Collect.objects.filter(resource_id=movie_id,column=2,user_id=user_id)# 查询关注此书的用户
        # 生成关注用户ID列表(int数据类型)
        if users_id.exists(): # 查找该用户是否在列表内，在则返回已关注，否则返回未关注
            return JsonResponse(
                {'errno': 0,
                 'data':{
                 'movie_id': movie.movie_id, 'name': movie.name, 'image': movie.image, 'director':movie.director,
                 'actor': movie.actor, 'year':movie.year, 'intro': movie.introduction, 'score': movie.score, 'heat': movie.heat},
                 'collect': 1})
        else:
            return JsonResponse(
                {'errno': 0,
                 'data': {
                     'movie_id': movie.movie_id, 'name': movie.name, 'image': movie.image, 'director': movie.director,
                     'actor': movie.actor, 'year': movie.year, 'intro': movie.introduction, 'score': movie.score,
                     'heat': movie.heat},
                 'collect': 0})

    else:
        return JsonResponse({'errno': 1000})
