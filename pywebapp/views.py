from django.db.models import Avg, Sum, Min, Q, F
from django.shortcuts import render, HttpResponse

from pywebapp.models import *


# Create your views here.

def index(req):
    return render(req, "index.html")


def addbook(req):
    # 方式1：
    # Book.objects.create(name="pyhhon", price=100, pub_date="2018-07-29", publish_id=4)
    # publish_obj = Publish.objects.filter(name="工业出版社")[0]
    # Book.objects.create(name="pyhhon", price=100, pub_date="2018-07-29", publish=publish_obj)
    # print(publish_obj)

    # 方式二：
    # query_set = Publish.objects.filter(name="机械出版社")
    # for k in query_set:
    #    print(k.book_set.all().values())

    # 方式三：
    # book_set = Book.objects.filter(publish__name="机械出版社").values("name", "price")
    # print(book_set)

    # ret = Publish.objects.filter(book__name="python").values("name")
    # print(ret)
    # ret2 = Book.objects.filter(name="python").values("publish__name")
    # print(ret2)
    #
    # ret3 = Book.objects.filter(publish__city="北京").values("name")
    # print(ret3)
    #
    # ret4 = Book.objects.filter(pub_date__lt="2018-07-30", pub_date__gt="2018-06-01").values("name")
    # print(ret4)

    # # 多对多，通过对象的方式绑定关系
    # book = Book.objects.get(id=2)
    # authors_object = book.authors
    # print(authors_object)
    #
    # # 反向查找
    # author_object = Author.objects.get(id=1)
    # set_all = author_object.book_set.all()
    # print(set_all)
    # book_obj = Book.objects.get(id=2)
    # author_objs = Author.objects.get(id=2)#添加多条
    # book_obj.authors.add(author_objs)

    # book_obj = Book.objects.get(id=2)
    # author_objs = Author.objects.all()#多条
    # book_obj.authors.add(*author_objs)#添加多条

    # book_obj = Book.objects.get(id=1)
    # author_objs=book_obj.objects.all()
    # book_obj.authors.remove(*author_objs)
    # book_obj.authors.remove(0, 1)  # 此处数字为对应书作者的id,支持多个id用逗号分割

    # 创建第三张表
    # Book_Author.objects.create(book_id=1, author_id=3)

    # set_all = Book.objects.get(id=1)
    # print(set_all.book_author_set.all()[0].author)

    # 多对多关联查询
    # ret = Book.objects.filter(book_author__author__name="lisi").values("name", "price")
    # print(ret)

    # book_obj = Book.objects.get(id=2)
    # author_objs = Author.objects.all()#多条
    # book_obj.authors.add(*author_objs)#添加多条
    #
    # ret = Book.objects.filter(authors__name="lisi").values("name", "price")
    # print(ret)

    # 【aggregate 聚合函数 ，求平均值】
    # avg_price = Book.objects.all().aggregate(Avg("price"))#平均值
    # sum_price = Book.objects.all().aggregate(Sum("price"))#和
    # sum_price = Book.objects.filter(authors__name="lisi").aggregate(mysum=Sum("price"))#可以取别名
    # print(avg_price)
    # print(sum_price)

    # 【annotate :分组】
    # ret = Book.objects.values("authors__name").annotate(Sum("price"))
    # print(ret)

    # min_price = Publish.objects.values("name").annotate(Min("book__price"))
    # print(min_price)

    #  F查询Q 查询
    # Book.objects.all().update(price=F("price")+10)

    # ret =Book.objects.filter(Q(price=110) | Q(name="java"))
    # print(ret)
    ret = Book.objects.filter(Q(price=110) | Q(name="scala"), name="java")  # Q 一定得放在前面
    print(ret)

    return HttpResponse("添加成功！")


def updatebook(req): pass


def delbook(req): pass


def selectbook(req): pass
