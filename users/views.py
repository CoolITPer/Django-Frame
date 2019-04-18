from django.http import HttpResponse, request
from django.shortcuts import render
from django.urls import reverse
from django_redis.serializers import json


def news(request, a, b):
    '''带参数的请求 reverse函数相当于flask中的url_for 传递匿名参数'''
    url=reverse('users:index')
    print(url)
    return HttpResponse("显示新闻：第%s 页第%s条" % (a, b))


'''query string 查询字符串传递 http://127.0.0.1:8000/news?category=1&page=2
    通过get方式请求参数'''
def news2(request):
    category = request.GET.get('category')
    page = request.GET.get('page')

    # ?category=1&page=2&a=3&a=4
    # a = request.GET.getlist('a')  # 一键多值通过 getlist 获取

    text = '获取查询字符串：<br/> category=%s, page=%s' % (category, page)
    return HttpResponse(text)
'''Django对POST、PUT、PATCH、DELETE请求方式开启了CSRF安全防护
    通过post方式请求参数 用postman来进行调试'''
def news3(request):
    category = request.POST.get('category')
    page = request.POST.get('page')

     # 一键多值通过从POST中用 getlist 获取
    # ?category=1&page=2&a=3&a=4
    # a = request.POST.getlist('a')

    text = '获取body中的键值对:<br/>　category=%s, page=%s' % (category, page)
    return HttpResponse(text)

'''非表单类型的请求体数据，Django无法自动解析，
    可以通过request.body属性获取最原始的请求体数据，自己按照请求体格式（JSON、XML等）进行解析'''
def news4(request):
    # 获取json字符串
    json_str = request.body
    json_str = json_str.decode()

    # 解析json
    dict_data = json.loads(json_str)
    category = dict_data.get('category')
    page = dict_data.get('page')

    text = '获取body中的json数据:　category=%s, page=%s' % (category, page)
    return HttpResponse(text)

def index(request):
    # render返回的是HttpResponse对象 返回模板页面
    return render(request, 'index.html')


def set_cookie(request):
    """保存cookie键值对数据"""
    response = HttpResponse('保存cookie数据成功')
    response.set_cookie('user_id', 10)
    response.set_cookie('user_name', 'admin')
    return response


def get_cookie(request):
    """读取cookie键值对数据"""
    user_id = request.COOKIES.get('user_id')
    user_name = request.COOKIES.get('user_name')
    text = 'user_id = %s, user_name = %s' % (user_id, user_name)
    return HttpResponse(text)


def set_session(request):
    """保存session键值对数据"""
    request.session['user_id'] = 10
    request.session['user_name'] = 'admin'
    return HttpResponse('保存session成功')


def get_session(request):
    """读取session键值对数据"""
    user_id = request.session.get('user_id')
    user_name = request.session.get('user_name')
    text = 'user_id = %s, user_name = %s' % (user_id, user_name)
    return HttpResponse(text)
