from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status, permissions
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from .models import *
from .serializers import *
from django.http import HttpResponse
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.views import View
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from . import permissions as mypermissions
from .throttling import MyAnon,MyUser
from .pagination import MyPagination
# Create your views here.


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryViewSets2(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(methods=['GET'], detail=False)
    def getlatestcagory(self, request):
        serialize = CategorySerializer(instance=Category.objects.all()[0:3], many=True)
        return Response(data=serialize.data, status=status.HTTP_200_OK)


class CategoryListView2(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CategoryDetailView2(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.delete(request, pk)


class CategoryListView1(APIView):
    '''
    1.继承django自带的View类需要重写对应的http方法
    2.继承DRF自带的APIView 类即可完成请求的响应封装，
    '''

    def get(self, request):
        # instance 从数据库取数据
        serialize = CategorySerializer(instance=Category.objects.all(), many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def post(self, request):
        # data 从请求中取数据
        serialize = CategorySerializer(data=request.data)
        # if serialize.is_valid():
        #     serialize.save()
        #     return Response(serialize.data,status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
        # 第二种方法
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(serialize.data, status=status.HTTP_200_OK)


class CategoryDetailView1(APIView):
    def get(self, request, cid):
        serialize = CategorySerializer(instance=get_object_or_404(Category, pk=cid))
        return Response(serialize.data, status=status.HTTP_200_OK)

    def put(self, request, cid):
        serialize = CategorySerializer(instance=get_object_or_404(Category, pk=cid), data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_200_OK)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, cid):
        serialize = CategorySerializer(instance=get_object_or_404(Category, pk=cid), data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_200_OK)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cid):
        get_object_or_404(Category, pk=cid).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        queryset = Category.objects.all()
        serialize = CategorySerializer(instance=queryset, many=True)
        print(serialize.data)
        return Response(serialize.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serialize = CategorySerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def category_detail(request, cid):
    model = get_object_or_404(Category, pk=cid)
    if request.method == 'GET':
        serialize = CategorySerializer(instance=model)
        return Response(serialize.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serialize = CategorySerializer(instance=model, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_200_OK)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return HttpResponse('路由不允许' + request.method + '操作')


class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承ModelViewSet 之后拥有GET POST PUT PATCH DELETE 等HTTP动作
    queryset 指明 需要操作的模型表
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # 自定义访问次数
    throttle_classes = [MyUser, MyAnon]
    # 自定义显示页码
    pagination_class = MyPagination
    # 用户未登录不显示分类列表，优先级高于全局配置
    # permission_classes = [permissions.IsAdminUser]

    # 超级管理员可以创建分类 普通用户可以查看分类
    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            return [permissions.IsAdminUser()]
        else:
            return []


class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class GoodImgsViewSets(viewsets.ModelViewSet):
    queryset = GoodImg.objects.all()
    serializer_class = GoodImgsSerializer

# 创建用户视图类
class UserViewSets1(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['POST'], detail=False)
    def regist(self, request):
        serialize = UserRegistSerialize(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(serialize.data, status=status.HTTP_201_CREATED)

class UserViewSets(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):

    '''
    声明用户资源类 用户操作：获取个人信息，更新个人信息，删除账户，创建账户
    扩展出action 路由，
    '''
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegistSerialize
        return UserSerializer

class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerialize

    def get_permissions(self):
        '''
        超级管理员只可以展示所有订单
        普通用户  可以创建修改订单 不可以操作其他用户订单
        :return:
        '''
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'retrieve' or self.action == 'destroy':
            return [mypermissions.OrdersPermission()]
        else:
            return [permissions.IsAdminUser()]
