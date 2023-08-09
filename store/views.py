from django.shortcuts import render
from django.http import HttpResponse
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status, generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import *


from .models import Product, Category
from .serializers import ProductSerializer


class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ProductAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )
    # permission_classes = (IsOwnerOrReadOnly, )


class ProductAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)


def index(request):
    product = Product.objects.all()
    return render(request, 'product.html', {'products': product})
    # return render(request, 'product.html')  # , {'products': product})
