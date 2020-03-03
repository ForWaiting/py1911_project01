from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from .models import *
from .serializers import *
from django.http import HttpResponse
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.views import View
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins


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


class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class GoodImgsViewSets(viewsets.ModelViewSet):
    queryset = GoodImg.objects.all()
    serializer_class = GoodImgsSerializer

# 创建用户视图类
class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['POST'], detail=False)
    def regist(self, request):
        serialize = UserRegistSerialize(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(serialize.data, status=status.HTTP_201_CREATED)
