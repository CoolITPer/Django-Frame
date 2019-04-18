from django.conf.urls import url

from DepartmentAdmin import views

urlpatterns = [
    url(r'/',views.show)
]