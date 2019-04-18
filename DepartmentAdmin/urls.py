from django.conf.urls import url

from DepartmentAdmin import views

urlpatterns = [
    url(r'^books/$', views.BookListView.as_view()),
    #?p<取名>
    url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view())
]