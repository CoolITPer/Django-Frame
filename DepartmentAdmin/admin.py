from django.contrib import admin
from DepartmentAdmin.models import Department, Employee, TestUser, HeroInfo, BookInfo

# '''将需要管理的板块添加到这里'''
# admin.site.register(Department)
# admin.site.register(Employee)


from django.contrib import admin

admin.site.site_title = 'Django OA' #网站标题
admin.site.site_header = '部门OA系统' #页面标题
admin.site.index_title = '欢迎使用Django' #页面标语

'''django管理后台可以实现对关联数据的编辑，例如：在编辑部门时，可以显示出该部门关联的所有员工对象，并进行编辑'''
class DepartmentStackedInline(admin.StackedInline):
    model = Employee  # 关联对象类型
    extra=5  #一次显示几条关联数据

class DepartmentTabularInline(admin.TabularInline):
    model = Employee  # 关联对象类型

# Register your models here.
'''自定义站点显示'''
class DepartmentAdmin(admin.ModelAdmin):
    # 搜索部门名称
    search_fields = ['name']
    '''也可以将自定义函数显示出来'''
    # 指定要显示的属性
    list_display = ["id", "name","GetTime"]
    # inlines = [DepartmentTabularInline]  # 栈的方式显示
    inlines = [DepartmentStackedInline]  # 表格样式显示

class EmployeeAdmin(admin.ModelAdmin):
    # 指定要显示的属性
    list_display = ["id", "name", "age", "gender", "comment", "department"]
    list_per_page = 5  # 每页显示5条，默认为100
    list_filter = ['gender', 'department'] # 显示过滤栏: 按性别和部门过滤

    # # 指定是编辑表中的哪些字段可以修改
    # fields = ['name', "age", "department"]
    fieldsets = (
        ('基本', {'fields': ('name', 'age', 'gender')}),
        ('高级', {'fields': ('comment', 'department'),
                 'classes':('collapse',)}),#默认为折叠字段
    )



# 参数2： 注册Admin类
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(TestUser)
admin.site.register(BookInfo)
admin.site.register(HeroInfo)
