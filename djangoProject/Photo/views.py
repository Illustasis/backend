import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from Photo.models import *


# 上传
@csrf_exempt
def upload_photo(request):
    if request.method == 'POST':
        photo = request.POST.get('photo', '')
        resource_id = request.POST.get('resource_id', '')
        resource_type = request.POST.get('resource_type', '')
        resource = Photos.objects.filter(resource_id=resource_id).filter(column=resource_type)
        if resource.exists():
            if resource_type == '1':  # 种类是用户头像时
                resource.delete()
                resource2 = Photos.objects.create(photo=photo, resource_id=resource_id, column=resource_type)
                resource2.save()
                return JsonResponse({'成功01': 200})
            elif resource_type == '2':  # 种类是文章图片时
                if len(resource) < 3:
                    resource3 = Photos.objects.create(photo=photo, resource_id=resource_id, column=resource_type)
                    resource3.save()
                    return JsonResponse({'成功02': 200})
                else:
                    return JsonResponse({'失败，达到图片上传数量上限': 100})

            else:
                return JsonResponse({'失败，资源种类有误': 100})
        else:
            if resource_type == '1' or resource_type == '2':
                resource4 = Photos.objects.create(photo=photo, resource_id=resource_id, column=resource_type)
                resource4.save()
                return JsonResponse({'成功03': 200})
            else:
                return JsonResponse({'失败，资源种类有误': 100})


# 获取图片
@csrf_exempt
def get_photo(request):
    if request.method == 'POST':
        resource_id = request.POST.get('resource_id', '')
        resource_type = request.POST.get('resource_type', '')
        resource = Photos.objects.filter(resource_id=resource_id).filter(column=resource_type)
        if resource.exists():
            for r in resource:
                return JsonResponse({'photo': r.photo})  # 这里还有问题，不知道怎么把ImageField传到前端
        else:
            return JsonResponse({'请求失败，无图片': 100})
    else:
        return JsonResponse({'失败，请求方式有误': 100})

