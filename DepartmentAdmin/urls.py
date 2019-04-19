from django.conf.urls import url

from DepartmentAdmin import views2, views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # url(r'^books/$', views.BookListView.as_view()),
    # #?p<取名>
    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view()),

    url(r'^books/$', views.BookInfoViewSet.as_view({'get': 'list'})),
    url(r'^books/latest/$', views.BookInfoViewSet.as_view({'get': 'latest'})),
    url(r'^books/(?P<pk>\d+)/$', views.BookInfoViewSet.as_view({'get': 'retrieve'})),
    url(r'^books/(?P<pk>\d+)/read/$', views.BookInfoViewSet.as_view({'put': 'read'})),
]




# router = DefaultRouter()  # 可以处理视图的路由器
# router.register(r'books', views2.BookInfoViewSet)  # 向路由器中注册视图集
# urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中