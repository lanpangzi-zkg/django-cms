#coding utf-8
from cms.models import Channel
def nav(request):
    channels=Channel.objects.all().order_by('order_position').filter(is_nav='1').filter(is_valid='1')
    return {'headerNav':channels}