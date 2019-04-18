from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View


def index(request):
    print('==index==')
    return HttpResponse('hello django')

def check_ip(view_fun):
    """装饰器：禁止黑名单ip访问"""
    def wrapper(request, *args, **kwargs):
        # 在视图函数执行前做额外的操作：
        # 禁止ip黑名单访问
        IP = request.META.get('REMOTE_ADDR')
        if IP in ['192.168.210.160']:
            return HttpResponse('IP禁止访问')
        #将视图函数进行返回
        return view_fun(request, *args, **kwargs)

    return wrapper

'''方法2 直接在类视图函数中进行装饰'''
class PostView(View):
    @method_decorator(check_ip)
    def get(self, request):
        """get请求： 显示发帖界面"""
        return HttpResponse('执行get操作')

    def post(self, request):
        """post请求： 执行发帖操作"""
        # 代码简略
        return HttpResponse('执行发帖操作')


'''方案3 使用多继承方式'''
class ListModelMixin(object):
    """
    list扩展类
    """
    def list(self, request, *args, **kwargs):
        print('查询多条数据')

class CreateModelMixin(object):
    """
    create扩展类
    """
    def create(self, request, *args, **kwargs):
        print('新增一条数据')

class DepartmentView(CreateModelMixin, ListModelMixin, View):
    """
    同时继承两个扩展类，复用list和create方法
    """
    def get(self, request):
        self.list(request)

    def post(self, request):
        self.create(request)

class EmployeeView(CreateModelMixin, View):
    """
    继承CreateModelMixin扩展类，复用create方法
    """
    def post(self, request):
        self.create(request)


def block(request):
    '''渲染模板'''
    context = {
        'name': 'django',
        'my_list': ['python', 'java', 'php', 'c/c++'],
        'my_dict': {
            'name': 'python',
            'age': 20,
            'gender': '男',
        }
    }
    return render(request, 'block.html', context)