from .views import ProductsRudView, ProductsAPIView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', ProductsAPIView.as_view(), name='post-create'),
    url(r'^(?P<id>\d+)/$', ProductsRudView.as_view(), name='post-rud'),
]
