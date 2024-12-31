from django.db import models


class Author(models.Model):
    name = models.CharField("作者姓名", max_length=100)
    age = models.IntegerField("年龄")
    phoneNum = models.CharField("电话号码", max_length=11)
    email = models.EmailField("邮箱")
    address = models.TextField("地址")


class OriginWork(models.Model):
    title = models.CharField("原作题目", max_length=100)
    pub_date = models.DateTimeField("发布日期")
    content = models.TextField("内容")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class DerivativeDevelopeDepartment(models.Model):
    name = models.CharField("开发商名称", max_length=100)
    address = models.TextField("地址")
    phoneNum = models.CharField("电话号码", max_length=11)


class DevelopTeam(models.Model):
    name = models.CharField("团队名称", max_length=100)
    leader = models.CharField("团队负责人", max_length=100)
    phoneNum = models.CharField("电话号码", max_length=11)
    email = models.EmailField("邮箱")
    address = models.TextField("地址")


class Product(models.Model):
    title = models.CharField("产品名称", max_length=100)
    pub_date = models.DateTimeField("发布日期")
    content = models.TextField("内容")
    price = models.FloatField("价格")
    version = models.CharField("版本号", max_length=100)


class Authorize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    department = models.ForeignKey(DerivativeDevelopeDepartment,
                                   on_delete=models.CASCADE)
    origin_work = models.ForeignKey(OriginWork, on_delete=models.CASCADE)
    authorize_date = models.DateTimeField("授权日期")
    authorize_period = models.IntegerField("授权期限")
    authorize_fee = models.FloatField("授权费用")


class ProductionCommission(models.Model):
    department = models.ForeignKey(DerivativeDevelopeDepartment,
                                   on_delete=models.CASCADE)
    team = models.ForeignKey(DevelopTeam, on_delete=models.CASCADE)
    commission_date = models.DateTimeField("委托日期")
    commission_fee = models.FloatField("委托费用")
