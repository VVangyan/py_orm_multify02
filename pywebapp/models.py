from django.db import models


# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateField()
    # 外键 models.ForeignKey("Publish") ,括号中为要关联的那张表，默认关联主键
    # publish = models.ForeignKey(Publish)  若不用引号那么Publish 必须定义在Book 之前
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)
    authors = models.ManyToManyField("Author")  # 推荐自动创建的

    def __str__(self):
        return self.name


class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)


# class Book_Author(models.Model):
#     book = models.ForeignKey("Book", on_delete=models.CASCADE)
#     author = models.ForeignKey("Author", on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=20)

    def __str__(self):
        return self.name
