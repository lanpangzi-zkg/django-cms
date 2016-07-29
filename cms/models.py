#coding utf-8
from django.db import models
import django.utils.timezone as timezone
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
class Channel(models.Model):
	Y_N=(
 		('1','是'),
 		('0','否'),
 	)
	channel_name=models.CharField('栏目名称',max_length=10,unique=True)
	is_nav=models.CharField('导航菜单',max_length=1,choices=Y_N,default='1')
	order_position=models.IntegerField('序列号',default=0)
	add_time=models.DateField('添加日期',auto_now_add=True, blank=True)
	is_single_page=models.CharField('单页栏目',max_length=1,choices=Y_N,default='0')
	is_valid=models.CharField('是否有效',max_length=1,choices=Y_N,default='1')
	
	def __str__(self):
		return self.channel_name
	def has_delete_permission(self,request):
		return False
	def has_add_permission(self,request):
		print("has_add_permission");
		return False
class Article(models.Model):
 	CHECK_STATE=(
 		('0','未审核'),
 		('1','审核通过'),
 		('2','审核未通过'),
 	)
 	Y_N=(
 		('0','是'),
 		('1','否'),
 	)
 	article_name=models.CharField('文章标题',max_length=30,null=False)
 	article_icon=models.ImageField('文章图片',upload_to='article',null=True)
 	article_guidance=models.CharField('文章导读',max_length=40,null=False,default='')
 	article_content=RichTextField('内容')
 	channel=models.ForeignKey(Channel,on_delete=models.CASCADE,verbose_name='所属栏目')
 	add_date=models.DateField('添加日期',auto_now_add=True, blank=True)
 	keys=models.CharField('关键字',max_length=50)
 	article_from=models.CharField('文章来源',max_length=50)
 	modify_date=models.DateField(auto_now=True, null=True)
 	add_user=models.CharField('作者',max_length=15)
 	check=models.CharField('审核状态',max_length=1,choices=CHECK_STATE,default='0')
 	visit=models.IntegerField('访问量',default=0)
 	def save(self,*args,**kwargs):
 		if self.id is None and self.channel.is_single_page=='1':
 			print(len(self.channel.article_set.all()))
 			if(len(self.channel.article_set.all())>=1):
 				raise ValidationError('文章所属栏目只能添加一篇文章') 
 			else:
 				print('add')
 				super(Article,self).save(*args,**kwargs)
 		else:
 			super(Article,self).save(*args,**kwargs)
class Banner(models.Model):
	banner_name=models.CharField('横幅名称',max_length=10,null=False)
	banner_url=models.CharField('链接地址',max_length=50)
	banner_image=models.ImageField('图片文件',upload_to='banner',null=False)
	banner_txt=models.CharField("描述文字",max_length=50)
	add_date=models.DateField(default=timezone.now,blank=True)
	def __str__(self):
		return self.banner_name

