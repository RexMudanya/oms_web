from django.db.models import Q
from rest_framework import generics, mixins
from omsApp.models import Product, ProductType
from .serializers import ProductSerializer, ProductTypeSerializer
from .permissions import IsOwnerOrReadOnly


class ProductTypeRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ProductTypeSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return ProductType.objects.all()


class ProductTypeAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ProductTypeSerializer
    queryset = ProductType.objects.all()

    def get_queryset(self):
        qs = ProductType.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(type__icontains=query) | Q(description__icontains=query)).distinct()
        return qs


class ProductsAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    lookup_field = 'id'  # url(r'?P<pk>\d+')
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        qs = Product.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(name__icontains=query) | Q(image__icontains=query)).distinct()
        return qs

    # needs user authentication to create which is a read only in serializers
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # built in method to handle a create call
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductsRudView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'id'  # url(r'?P<pk>\d+')
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
    # queryset = Product.objects.all()

    def get_queryset(self):
        return Product.objects.all()

    # def get_object(self):
        # return Product.objects.all()
