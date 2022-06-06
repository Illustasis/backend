from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from Search.models import *


# 图书相关搜索
@csrf_exempt
def book_search(request):
    if request.method == 'POST':
        search_id = request.POST.get('search_id')
        search_content = request.POST.get('search_content')
        if search_id == '11':  # 按书名
            books = Book.objects.filter(name__icontains=search_content)  # 返回包含查询内容的图书列表(不区分大小写)
            if books.exists():
                booklist = []
                for b in books:
                    booklist.append({
                        'name': b.name,
                        'image': b.image,
                        'author': b.author,
                        'id': b.book_id
                    })
                return JsonResponse({'errno': 0, 'msg': '按书名查询', 'data': booklist})
            else:
                return JsonResponse({'errno': 1001, 'msg': '未找到相关图书'})
        elif search_id == '12':  # 按作者
            books = Book.objects.filter(author__icontains=search_content)
            if books.exists():
                booklist = []
                for b in books:
                    booklist.append({
                        'name': b.name,
                        'image': b.image,
                        'author': b.author,
                        'id': b.book_id
                    })
                return JsonResponse({'errno': 0, 'msg': '按图书作者查询', 'data': booklist})
            else:
                return JsonResponse({'errno': 1001, 'msg': '未找到相关图书'})
        elif search_id == '13':  # 按简介
            books = Book.objects.filter(introduction__icontains=search_content)
            if books.exists():
                booklist = []
                for b in books:
                    booklist.append({
                        'name': b.name,
                        'image': b.image,
                        'author': b.author,
                        'id': b.book_id
                    })
                return JsonResponse({'errno': 0, 'msg': '按图书简介查询', 'data': booklist})
            else:
                return JsonResponse({'errno': 1001, 'msg': '未找到相关图书'})
        else:
            return JsonResponse({'errno': 1002, 'msg': '查询编码错误'})


# 电影相关搜索
@csrf_exempt
def movie_search(request):
    if request.method == 'POST':
        search_id = request.POST.get('search_id')
        search_content = request.POST.get('search_content')
        if search_id == '21':  # 按电影名
            movies = Movie.objects.filter(name__icontains=search_content)  # 返回包含查询内容的电影列表(不区分大小写)
            if movies.exists():
                movielist = []
                for m in movies:
                    movielist.append({
                        'name': m.name,
                        'image': m.image,
                        'director': m.director,
                        'id': m.movie_id
                    })
                return JsonResponse({'errno': 0, 'msg': '按电影名查询', 'data': movielist})
            else:
                return JsonResponse({'errno': 1001, 'msg': '未找到相关电影'})
        elif search_id == '22':  # 按导演
            movies = Movie.objects.filter(director__icontains=search_content)
            if movies.exists():
                movielist = []
                for m in movies:
                    movielist.append({
                        'name': m.name,
                        'image': m.image,
                        'director': m.director,
                        'id': m.movie_id
                    })
                return JsonResponse({'errno': 0, 'msg': '按电影导演查询', 'data': movielist})
            else:
                return JsonResponse({'errno': 1001, 'msg': '未找到相关电影'})
        elif search_id == '23':  # 按演员
            movies = Movie.objects.filter(actor__icontains=search_content)
            if movies.exists():
                movielist = []
                for m in movies:
                    movielist.append({
                        'name': m.name,
                        'image': m.image,
                        'director': m.director,
                        'id': m.movie_id
                    })
                return JsonResponse({'errno': 0, 'msg': '按电影演员查询', 'data': movielist})
            else:
                return JsonResponse({'errno': 1001, 'msg': '未找到相关电影'})
        elif search_id == '24':  # 按简介
            movies = Movie.objects.filter(introduction__icontains=search_content)
            if movies.exists():
                movielist = []
                for m in movies:
                    movielist.append({
                        'name': m.name,
                        'image': m.image,
                        'director': m.director,
                        'id': m.movie_id
                    })
                return JsonResponse({'errno': 0, 'msg': '按电影简介查询', 'data': movielist})
            else:
                return JsonResponse({'errno': 1001, 'msg': '未找到相关电影'})
        else:
            return JsonResponse({'errno': 1002, 'msg': '查询编码错误'})


# 电视剧相关查询
@csrf_exempt
def tele_search(request):
    if request.method == 'POST':
        search_id = request.POST.get('search_id')
        search_content = request.POST.get('search_content')
        if search_id == '31':  # 按电视剧名
            teles = Tele.objects.filter(name__icontains=search_content)  # 返回包含查询内容的电视剧列表(不区分大小写)
            if teles.exists():
                telelist = []
                for t in teles:
                    telelist.append({
                        'name': t.name,
                        'image': t.image,
                        'year': t.year,
                        'nation': t.nation,
                        'id': t.tele_id
                    })
                return JsonResponse({'errno': 0, 'msg': '按电视剧名查询', 'data': telelist})
            else:
                return JsonResponse({'errno': 1001, 'msg': '未找到相关电视剧'})
        elif search_id == '32':  # 按演员
            teles = Tele.objects.filter(actor__icontains=search_content)
            if teles.exists():
                telelist = []
                for t in teles:
                    telelist.append({
                        'name': t.name,
                        'image': t.image,
                        'year': t.year,
                        'nation': t.nation,
                        'id': t.tele_id
                    })
                return JsonResponse({'errno': 0, 'msg': '按电视剧演员查询', 'data': telelist})
            else:
                return JsonResponse({'errno': 1001, 'msg': '未找到相关电视剧'})
        elif search_id == '33':  # 按简介
            teles = Tele.objects.filter(introduction__icontains=search_content)
            if teles.exists():
                telelist = []
                for t in teles:
                    telelist.append({
                        'name': t.name,
                        'image': t.image,
                        'year': t.year,
                        'nation': t.nation,
                        'id': t.tele_id
                    })
                return JsonResponse({'errno': 0, 'msg': '按电视剧简介查询', 'data': telelist})
            else:
                return JsonResponse({'errno': 1001, 'msg': '未找到相关电视剧'})
        else:
            return JsonResponse({'errno': 1002, 'msg': '查询编码错误'})


# 话题查询
@csrf_exempt
def topic_search(request):
    if request.method == 'POST':
        search_id = request.POST.get('search_id')
        search_content = request.POST.get('search_content')
        if search_id == '41':  # 按话题名
            topics = Topic.objects.filter(name__icontains=search_content)
            if topics.exists():
                topiclist = []
                for t in topics:
                    topiclist.append({
                        'name': t.name,
                        'id': t.topic_id
                    })
                return JsonResponse({'errno': 0, 'msg': '按话题名查询', 'data': topiclist})
            else:
                return JsonResponse({'errno': 1001, 'msg': '未找到相关话题'})
        elif search_id == '42':  # 按话题简介
            topics = Topic.objects.filter(introduction__icontains=search_content)
            if topics.exists():
                topiclist = []
                for t in topics:
                    topiclist.append({
                        'name': t.name,
                        'id': t.topic_id
                    })
                return JsonResponse({'errno': 0, 'msg': '按话题简介查询', 'data': topiclist})
            else:
                return JsonResponse({'errno': 1001, 'msg': '未找到相关话题'})
        else:
            return JsonResponse({'errno': 1002, 'msg': '查询编码错误'})


# 小组
@csrf_exempt
def group_search(request):
    if request.method == 'POST':
        search_id = request.POST.get('search_id')
        search_content = request.POST.get('search_content')
        if search_id == '51':  # 按小组名
            groups = Group.objects.filter(name__icontains=search_content)
            if groups.exists():
                grouplist = []
                for g in groups:
                    grouplist.append({
                        'name': g.name,
                        'id': g.group_id
                    })
                return JsonResponse({'errno': 0, 'msg': '按小组名查询', 'data': grouplist})
            else:
                return JsonResponse({'errno': 1001, 'msg': '未找到相关小组'})
        else:
            return JsonResponse({'errno': 1002, 'msg': '查询编码错误'})


# 文章
@csrf_exempt
def article_search(request):
    if request.method == 'POST':
        search_id = request.POST.get('search_id')
        search_content = request.POST.get('search_content')
        if search_id == '61':  # 按文章名
            articles = Article.objects.filter(title__icontains=search_content)
            if articles.exists():
                articlelist = []
                for a in articles:
                    articlelist.append(a)
                return JsonResponse({'errno': 0, 'msg': '按文章名查询', 'data': articlelist})
            else:
                return JsonResponse({'errno': 1001, 'msg': '未找到相关文章'})
        else:
            return JsonResponse({'errno': 1002, 'msg': '查询编码错误'})
