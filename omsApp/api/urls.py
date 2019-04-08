from .views import ProductsRudView, ProductsAPIView, ProductTypeRudView, ProductTypeAPIView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', ProductsAPIView.as_view(), name='post-create'),
    url(r'^(?P<id>\d+)/$', ProductsRudView.as_view(), name='post-rud'),
    url(r'^$', ProductTypeAPIView.as_view(), name='post-create-productType'),
    url(r'^(?P<id>\d+)/$', ProductTypeRudView.as_view(), name='post-rud-productType'),
]

