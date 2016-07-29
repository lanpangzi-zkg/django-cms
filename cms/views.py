from django.shortcuts import render
from .models import Channel,Article,Banner
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
#首页
def index(request):
    banners=Banner.objects.all()
    hyzx_channel=Channel.objects.get(channel_name='行业资讯')
    hyzx_articles=hyzx_channel.article_set.all().order_by('-add_date')[:6]
    tzgg_channel=Channel.objects.get(channel_name='通知公告')
    tzgg_articles=tzgg_channel.article_set.all().order_by('-add_date')[:3]
    hydt_channel=Channel.objects.get(channel_name='会员动态')
    hydt_articles=hydt_channel.article_set.all().order_by('-add_date')[:3]
    return render(request,'index.html',{'banners':banners,'hyzx_channel_id':hyzx_channel.id,'hyzx_articles':hyzx_articles,
        'tzgg_articles':tzgg_articles,'tzgg_channel_id':tzgg_channel.id,'hydt_articles':hydt_articles,'hydt_channel_id':hydt_channel.id,})
#栏目下面的文章信息
def channel(request,channel_id):
    chs=Channel.objects.get(id=channel_id)
    if chs.is_single_page == '1':
        try:
            single_article=chs.article_set.all()[0]#取第一篇文章
        except IndexError:
            single_article=None
        return render(request,'channel.html',{'is_single_page':chs.is_single_page,'channel_name':chs.channel_name,'single_article':single_article})
    else:       
        articles=chs.article_set.all()#外键查询
        paginator=Paginator(articles,6)
        page=request.GET.get('page')
        try:
            articles_page=paginator.page(page)
        except PageNotAnInteger:
            articles_page=paginator.page(1)
        except EmptyPage:
            articles_page=paginator.page(paginator.num_pages)    
        return render(request,'channel.html',{'is_single_page':chs.is_single_page,
            'channel_name':chs.channel_name,'artlist':articles_page,'count':len(articles)})
#根据文章id查询文章详细内容
def articleDetails(request,article_id):
    art=Article.objects.get(id=article_id)
    art.visit=art.visit+1
    art.save()
    return render(request,'article.html',{'art':art})