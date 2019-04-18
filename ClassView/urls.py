from django.conf.urls import url

from ClassView import views
from ClassView.views import check_ip

urlpatterns = [
    #方案1 直接在路由中进行装饰
    # url(r'^post2$', check_ip(views.PostView.as_view())),
    url(r'^post2$', views.PostView.as_view()),
    url(r'^index$',views.index),
    url(r'^block$',views.block)
]