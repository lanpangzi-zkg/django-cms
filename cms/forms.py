from django import forms

#首页滚动横幅
class Banner(forms.Form):
    banner_name=forms.CharField(max_length=10)
    banner_txt=forms.CharField(max_length=50)
    banner_url=forms.CharField(max_length=20)
    banner_image=forms.FileField()
    add_date=forms.DateField(auto_now_add=True, blank=True)
