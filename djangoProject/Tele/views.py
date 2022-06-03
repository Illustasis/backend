from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from System.models import *
import json
# Create your views here.
@csrf_exempt
def hot(request):
    if request.method == 'POST':
        num = request.POST.get('num')
        telelist=Tele.objects.all().order_by('heat').all()
        hottelelist=[]
        i=0
        while i<10:
            hottelelist.append({
                'name':telelist[i].name,
                'image':telelist[i].image,
                'year':telelist[i].year,
                'nation':telelist[i].nation,
                'id':telelist[i].tele_id
            })
            i=i+1
        return JsonResponse({'errno':0,'msg':'查询热门电影','data':hottelelist})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

@csrf_exempt
def high(request):
    if request.method == 'POST':
        num = request.POST.get('num')
        telelist=Tele.objects.all().order_by('score').all()
        hightelelist=[]
        i=0
        while i<10:
            hightelelist.append({
                'name':telelist[i].name,
                'image':telelist[i].image,
                'year':telelist[i].year,
                'nation':telelist[i].nation,
                'id':telelist[i].tele_id
            })
            i=i+1
        return JsonResponse({'errno':0,'msg':'查询热门电影','data':hightelelist})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

@csrf_exempt
def collect(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        tele_id = request.POST.get('tele_id')
        collect = Collect(resource_id=tele_id, column=3, user_id=user_id)
        collect.save()
        return JsonResponse({'errno':0, 'msg': "收藏成功"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

@csrf_exempt
def uncollect(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        tele_id = request.POST.get('tele_id')
        collection = Collect.objects.filter(resource_id=tele_id, column=3, user_id=user_id)
        if collection.exists() :
            collect=Collect.objects.get(resource_id=tele_id, column=3, user_id=user_id)
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
        collections = Collect.objects.filter(user_id=user_id,column=3)
        print(collections)
        collect=[]
        for item in collections:
            tele = Tele.objects.get(tele_id=item.resource_id)
            collect.append({
                'id': tele.tele_id,
                'name':tele.name,
                'year':tele.year,
                'nation':tele.nation,
                'image':tele.image,
                'star':tele.score,
            })
        return JsonResponse({'errno':0, 'data':collect})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

@csrf_exempt
def detail(request):
    if request.method == 'POST':
        tele_id = request.POST.get('tele_id')  # 获取图书ID
        user_id = request.POST.get('user_id')  # 获取用户ID
        tele = Tele.objects.get(tele_id=tele_id)
        users_id = Collect.objects.filter(resource_id=tele_id,column=3,user_id=user_id)# 查询关注此书的用户
        # 生成关注用户ID列表(int数据类型)
        if users_id.exists(): # 查找该用户是否在列表内，在则返回已关注，否则返回未关注
            return JsonResponse(
                {'errno': 0,
                 'data':{
                 'tele_id': tele.tele_id, 'name': tele.name, 'image': tele.image, 'nation':tele.nation,
                 'actor': tele.actor, 'year':tele.year, 'intro': tele.introduction, 'score': tele.score, 'heat': tele.heat},
                 'collect': 1})
        else:
            return JsonResponse(
                {'errno': 0,
                 'data': {
                      'tele_id': tele.tele_id, 'name': tele.name, 'image': tele.image, 'nation':tele.nation,
                       'actor': tele.actor, 'year':tele.year, 'intro': tele.introduction, 'score': tele.score, 'heat': tele.heat},
                 'collect': 0})

    else:
        return JsonResponse({'errno': 1000})
