# -*-coding:utf-8-*-
from django.db import models


# Create your models here.
#职位名称,地区,薪水,标签,能力要求,公司名字,福利待遇,详情链接
class Occupation(models.Model):
    occupation = models.CharField(verbose_name="ְ职位名称", name='职位名称', max_length=32)
    area = models.CharField(verbose_name="地区",name='地区', max_length=32)
    salary = models.CharField(verbose_name="薪水",name='薪水', max_length=32)
    tag = models.CharField(verbose_name="标签",name='标签', max_length=32)
    ability = models.CharField(verbose_name="能力要求", name='能力要求',max_length=32)
    company = models.CharField(verbose_name="公司名字", name='公司名字',max_length=32)
    welfare = models.CharField(verbose_name="福利待遇", name='福利待遇',max_length=128)
    link = models.CharField(verbose_name="详情链接",name='详情链接', max_length=128)
#下次数据库要加id
    class Meta:
        db_table = 'jobs_origin'
