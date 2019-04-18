from django.contrib import admin
from DepartmentAdmin.models import Department, Employee

# '''将需要管理的板块添加到这里'''
# admin.site.register(Department)
# admin.site.register(Employee)


# Register your models here.
'''自定义站点显示'''
class DepartmentAdmin(admin.ModelAdmin):
    # 搜索部门名称
    search_fields = ['name']
    '''也可以将自定义函数显示出来'''
    def GetTime(self):
        return self.create_date.strftime('%Y-%m-%d')
    GetTime.short_description='创建时间'
    GetTime.admin_order_field='create_date'
    # 指定要显示的属性
    list_display = ["id", "name","GetTime"]

class EmployeeAdmin(admin.ModelAdmin):
    # 指定要显示的属性
    list_display = ["id", "name", "age", "gender", "comment", "department"]
    list_per_page = 5  # 每页显示5条，默认为100
    list_filter = ['gender', 'department'] # 显示过滤栏: 按性别和部门过滤

# 参数2： 注册Admin类
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
