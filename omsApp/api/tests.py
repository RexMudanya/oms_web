from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class ProductPostAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User(username='testuser', email='test@test.com')
        user_obj.set_password("123456")
        user_obj.save()
        product_post = ProductPostAPITestCase.objects.create(user=user_obj, name='', productType='', price='', image='')



