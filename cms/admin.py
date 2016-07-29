from django.contrib import admin
from .models import Channel,Article,Banner
# Register your models here.

class ChannelAdmin(admin.ModelAdmin):
	list_display=('channel_name','add_time')
	
class ArticleAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self,db_field,request,**kwargs):
        kwargs['queryset']=Channel.objects.all()
        # if(db_field.name=='channel'):
        #     kwargs['queryset']=Channel.objects.all().filter(is_single_page='0')
        return super(ArticleAdmin,self).formfield_for_foreignkey(db_field,request,**kwargs)
    list_display=('article_name','channel','check','add_date')

class BannerAdmin(admin.ModelAdmin):
    list_display=('banner_name','banner_image')

admin.site.register(Channel,ChannelAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Banner,BannerAdmin)