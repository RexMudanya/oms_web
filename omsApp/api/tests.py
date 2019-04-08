from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from omsApp.models import Product, ProductType
from rest_framework.reverse import reverse as api_reverse

User = get_user_model()


class ProductPostAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User(username='testuser', email='test@test.com')
        user_obj.set_password("123456")
        user_obj.save()
        productType_post = ProductType.objects.create(type='Snacks', description='small pickings')
        product_post = Product.objects.create(user=user_obj, name='cookie', productType='Snacks',
                                              price='200', image='/home/rex/Downloads/icon.jpg')

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_post(self):
        post_count = Product.objects.count()
        self.assertEqual(post_count, 1)
        post_count = ProductType.objects.count()
        self.assertGreaterEqual(post_count, 1)

    def get_api_url(self):
        return api_reverse("api-omsApp:post-rud", kwargs={'pk': self.pk})




