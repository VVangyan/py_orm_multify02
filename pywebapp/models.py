from django.db import models


# Create your models here.


# 【 Field重要参数:】
# <1> null ： 数据库中字段是否可以为空
# <2> blank： django的 Admin 中添加数据时是否可允许空值
# <3> default：设定缺省值
# <4> editable：如果为假，admin模式下将不能改写。缺省为真
# <5> primary_key：设置主键，如果没有设置django创建表时会自动加上：
#     id = meta.AutoField('ID', primary_key=True)
#     primary_key=True implies blank=False, null=False and unique=True. Only one
#     primary key is allowed on an object.
# <6> unique：数据唯一
# <7> verbose_name　　Admin中字段的显示名称
# <8> validator_list：有效性检查。非有效产生 django.core.validators.ValidationError 错误
# <9> db_column，db_index 如果为真将为此字段创建索引
# <10>choices：一个用来选择值的2维元组。第一个值是实际存储的值，第二个用来方便进行选择。
#             如SEX_CHOICES= (( ‘F’,'Female’),(‘M’,'Male’),)
#             gender = models.CharField(max_length=2,choices = SEX_CHOICES)


class Book(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名")  # verbose_name  admin 管理页面上面的别名称
    price = models.IntegerField("价格")  # 也可以直接写
    pub_date = models.DateField("日期")
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
