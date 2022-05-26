from django.db import models


class User(models.Model):
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    user_id = models.AutoField(primary_key=True)


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    image = models.CharField(max_length=200)  # 封面图片
    author = models.CharField(max_length=80)
    press = models.CharField(max_length=80)  # 出版社
    introduction = models.TextField(max_length=1000,default='')
    score = models.DecimalField(max_digits=1, decimal_places=1)  # 评分，5分满分，1位小数
    heat = models.IntegerField  # 点击量

    def __init__(self, name, image, author, press, intro, score, heat):
        models.Model.__init__(self)
        self.name = name
        self.imag = image
        self.author = author
        self.press = press
        self.introduction = intro
        self.score = score
        self.heat = heat


class Score(models.Model):  # 评分表
    user_id = models.IntegerField
    resource_id = models.IntegerField  # 相关资源（book,movie)的id
    score = models.IntegerField


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    text = models.TextField
    author_id = models.IntegerField
    date = models.DateTimeField(auto_now_add=True)
    heat = models.IntegerField
    column = models.IntegerField  # 分类 1:book,2:movie,3:topic
    resource_id = models.IntegerField  # 相关资源（book,movie,topic）的id
    likes = models.IntegerField


class Collect(models.Model):
    user_id = models.IntegerField
    resource_id = models.IntegerField  # 相关资源（book,movie,topic，group）的id
    column = models.IntegerField  # 分类 1:book,2:movie,3:topic,4:group


class Reply(models.Model):
    reply_id = models.AutoField(primary_key=True)
    article_id = models.IntegerField
    text = models.CharField(max_length=80)
    likes = models.IntegerField
    author_id = models.IntegerField
    reply_to = models.IntegerField
