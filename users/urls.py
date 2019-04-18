from django.conf.urls import url

from users import views

urlpatterns = [

    # 配置url和视图函数，需要调用url函数，并传入参数
    # 参数1： 匹配url的正则表达式（需要用 ^ 和 $ 匹配开头和结尾）
    # 参数2： url匹配成功执行的视图函数
    url(r'^index$', views.index,name='index'),
    url(r'^news/(\d+)/(\d+)$', views.news,name='news'),
    url(r'^news2$', views.news2),
    url(r'^news3$', views.news3),
    url(r'^set_cookie$', views.set_cookie),
    url(r'^get_cookie$', views.get_cookie),
    url(r'^set_session$', views.set_session),
    url(r'^get_session$', views.get_session),
]