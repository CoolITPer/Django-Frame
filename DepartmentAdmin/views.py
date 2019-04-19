from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

# url(r'^books/$', views.BookListView.as_view()),
from rest_framework.viewsets import GenericViewSet

from DepartmentAdmin.models import BookInfo
from DepartmentAdmin.serializers import BookInfoSerializer, BookInfoReadSerializer


class BookListView(APIView):
    '''后台给前端返回数据：查询--序列化--返回序列化数据'''
    def get(self, request):
        books = BookInfo.objects.all()
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data)

# url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view()),
class BookDetailView(GenericAPIView):
    queryset = BookInfo.objects.all() #指名查询数据集
    serializer_class = BookInfoSerializer  #指名序列化器

    def get(self, request, pk):
        book = self.get_object() # get_object()方法根据pk参数查找queryset中的数据对象，获取单一数据
        serializer = self.get_serializer(book)  #将数据序列化
        return Response(serializer.data)

'''同一个get方法对应两种不同的请求'''
# url(r'^books/$', BookInfoViewSet.as_view({'get':'list'}),
#url(r'^books/(?P<pk>\d+)/$', BookInfoViewSet.as_view({'get': 'retrieve'})
class BookInfoViewSet(viewsets.ViewSet):

    def list(self, request):
        books = BookInfo.objects.all()
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            books = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookInfoSerializer(books)
        return Response(serializer.data)


'''最简化的写法：不管是查询所有的书籍还是单个书籍都可以'''
class BookInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

class BookInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    '''根据action来指定不同的序列化器'''
    def get_serializer_class(self):
        if self.action == 'create':
            return BookInfoReadSerializer
        else:
            return BookInfoSerializer

    @action(methods=['get'], detail=False)
    def latest(self, request):
        """
        返回最新的图书信息
        """
        book = BookInfo.objects.latest('id')
        serializer = self.get_serializer(book)
        return Response(serializer.data)
    '''修改阅读量：取到对象本身--获取前台阅读量--保存数据（执行更新）--序列化--返回前端'''

    @action(methods=['put'], detail=True)
    def read(self, request, pk):
        """
        修改图书的阅读量数据
        """
        book = self.get_object()
        book.bread = request.data.get('read')
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)