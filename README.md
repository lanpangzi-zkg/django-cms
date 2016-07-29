# django-cms

最近在自学python,接触了python的web开发框架--django,自己学着搭建了一个简单CMS网站,效果图如下：
<div>
    <h3>首页：</h3>
    <img src="https://raw.githubusercontent.com/putaomogu/django-cms/master/rmimg/index.png" alt="首页">
</div>
<div>
    <h3>栏目：</h3>
    <img src="https://raw.githubusercontent.com/putaomogu/django-cms/master/rmimg/channel.png" alt="栏目">
</div>
<div>
    <h3>文章：</h3>
    <img src="https://raw.githubusercontent.com/putaomogu/django-cms/master/rmimg/article.png" alt="文章">
</div>
<div>
    <h3>管理主界面：</h3>
    <img src="https://raw.githubusercontent.com/putaomogu/django-cms/master/rmimg/admin.png" alt="管理主界面">
</div>
<div>
    <h3>栏目管理界面：</h3>
    <img src="https://raw.githubusercontent.com/putaomogu/django-cms/master/rmimg/admin_channel.png" alt="栏目管理界面">
</div>
<div>
    <h3>文章编辑界面：</h3>
    <img src="https://raw.githubusercontent.com/putaomogu/django-cms/master/rmimg/admin_eidt_a.png" alt="文章编辑界面">
</div>
<h1>开发说明：</h1>
<h2>1.开发工具</h2>
<p>
   <ul>
   <li>python</li>
   <li>包管理工具pip</li>
   <li>django</li>
   </ul>
</p>
<h2>2.项目创建</h2>
<p>
   <ul>
   <li>创建项目文件夹</li>
   <li>打开cmd命令，进入该文件夹，执行命令"django-admin startproject helloDjango"</li>
   <li>cmd进入包含manage.py目录,运行"python manage.py runserver"启动服务器</li>
   </ul>
</p>
<h2>3.项目结构说明</h2>
<p>
  <img src="https://raw.githubusercontent.com/putaomogu/django-cms/master/rmimg/project.png" alt="项目结构说明">
</p>
<h2>4.开发总结</h2>
<p> 
   <ul>
    <li>1.django自带数据库，因此在开发过程中直接使用该数据库，django也支持其他数据库；</li>
    <li>2.django框架功能很完善，帮助开发者封装了很多网站开发的步骤，因此可以写少量代码即可实现功能比较丰富的web站点；</li>
    <li>3.djando将库表映射成一个对象，因此操作起来十分方便与简单，让开发者不用关心具体的数据库操作；</li>
    <li>4.django通过urls.py配置来实现路由管理，该配置灵活且简单，可以轻松实现优雅的访问地址和RESTful风格API;</li>
    <li>5.django容许扩展Model对象，实现个性化需求。</li>
  </ul>
</p>
