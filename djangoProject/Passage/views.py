from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from System.models import *
import json

@csrf_exempt
def bookcomment(request):
    if request.method == 'POST':
        article_id = request.POST.get('article_id')
        article=Article.objects.get(article_id=article_id)
        print(Article.objects.all().values('article_id','author_id'))
        book=Book.objects.get(book_id=article.resource_id)
        user=User.objects.get(user_id=article.author_id)
        score=Score.objects.get(column=1,resource_id=article.resource_id,user_id=article.author_id)
        collect = Collect.objects.filter(column=6,resource_id=article_id)
        reply = Reply.objects.filter(article_id=article_id)
        content={
            'username':user.name,
            'user_id':user.user_id,
            'title':article.title,
            'content':article.text,
            'writer':book.author,
            'date':article.date,
            'star':score.score,
            'like':len(collect),
            'reply':len(reply)
        }
        resource={
            'name':book.name,
            'id':book.book_id,
            'star':book.score,
            'img':book.image,
            'writer':book.author,
        }
        return JsonResponse({'errno':0,'msg':'查询书评详情','data':{'passage':content,'resource':resource}})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})