# from django.utils.deprecation import MiddlewareMixin
#
#
# class MyMiddleware2(MiddlewareMixin):
#
#     def __init__(self, get_response=None):
#         super().__init__(get_response)
#         print('init 2')
#
#     def process_request(self, request):
#         print('before 视图 2')
#
#     def process_response(self, request, response):
#         print('after 视图 2')
#         return response
#
# class MyMiddleware(MiddlewareMixin):
#
#     def __init__(self, get_response=None):
#         super().__init__(get_response)
#         print('init')
#
#     def process_request(self, request):
#         print('before 视图')
#         # 注意：可以返回None或者response对象，如果返回response对象，则视图函数就不会再执行了
#
#     def process_response(self, request, response):
#         print('after 视图')
#         return response
#
#
# '''中间件执行顺序
#      before 视图
#      before 视图 2
#      ==index==
#      after 视图 2
#      after 视图'''