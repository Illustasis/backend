from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from System.models import *
import json

@csrf_exempt
def hotbook(request):
    if request.method == 'POST':
        num = request.POST.get('num')
        booklist=Book.objects.all().order_by('heat').all()
        hotbooklist=[]
        i=0
        while i<10:
            hotbooklist.append({
                'name':booklist[i].name,
                'image':booklist[i].image,
                'author':booklist[i].author,
                'id':booklist[i].book_id
            })
            i=i+1
        return JsonResponse({'errno':0,'msg':'查询热门图书','data':hotbooklist})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

@csrf_exempt
def collect(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        book_id = request.POST.get('book_id')
        collectbook = Collect(resource_id=book_id, column=1, user_id=user_id)
        collectbook.save()
        return JsonResponse({'errno':0, 'msg': "收藏成功"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

@csrf_exempt
def uncollect(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        book_id = request.POST.get('book_id')
        collectbook=Collect.objects.get(resource_id=book_id, column=1, user_id=user_id)
        collectbook.delete()
        return JsonResponse({'errno':200, 'msg': "已取消收藏"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
@csrf_exempt
def detail(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')  # 获取图书ID
        user_id = request.POST.get('user_id')  # 获取用户ID
        book = Book.objects.get(book_id=book_id)
        users_id = Collect.objects.filter(resource_id=book_id,column=1,user_id=user_id)# 查询关注此书的用户
        # 生成关注用户ID列表(int数据类型)
        if users_id.exists(): # 查找该用户是否在列表内，在则返回已关注，否则返回未关注
            return JsonResponse(
                {'errno': 0,
                 'data':{
                 'book_id': book.book_id, 'name': book.name, 'image': book.image, 'author': book.author,
                 'press': book.press, 'intro': book.introduction, 'score': book.score, 'heat': book.heat},
                 'collect': 1})
        else:
            return JsonResponse(
                {'errno': 0,
                 'data': {
                     'book_id': book.book_id, 'name': book.name, 'image': book.image, 'author': book.author,
                     'press': book.press, 'intro': book.introduction, 'score': book.score, 'heat': book.heat},
                     'collect': 0})

    else:
        return JsonResponse({'errno': 1000})


@csrf_exempt
def hot_article(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        articles = Article.objects.filter(columm=1).filter(article_id=book_id).order_by('-heat')  # 按照文章类型和文章ID查找
        article_list = []
        for article in articles:
            article_list.append(article)
        article_json = json.dumps({'value': article_list}, ensure_ascii=False)
        # 生成文章的JSON文件
        return JsonResponse({'成功': 200}, article_json)
    else:
        return JsonResponse({'失败，请求方式错误': 100})


@csrf_exempt
def new_article(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        articles = Article.objects.filter(columm=1).filter(article_id=book_id).order_by('-date')
        # 不确定这里是从早到晚排序还是从晚到早排序，测试时如果遇到相反的可以把order_by后面括号内的'-date'改成'date'
        article_list = []
        for article in articles:
            article_list.append(article)
        article_json = json.dumps({'value': article_list}, ensure_ascii=False)
        return JsonResponse({'成功': 200}, article_json)
    else:
        return JsonResponse({'失败，请求方式错误': 100})
