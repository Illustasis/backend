from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from System.models import *
import json

@csrf_exempt
def hottopic(request):
    if request.method == 'POST':
        num = request.POST.get('num')
        list=Topic.objects.all().order_by('heat').all()
        hotlist=[]
        i=0
        while i < int(num):
            hotlist.append({
                'name':list[i].name,
                'id':list[i].topic_id
            })
            i=i+1
        return JsonResponse({'errno':0,'msg':'查询热门话题','data':hotlist})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

