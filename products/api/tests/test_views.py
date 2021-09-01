from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from users.models import User
from branches.models import City
from addresses.models import Address
from products.models import Item
from branches.models import BranchItem, Branch, City
from django.contrib.gis.geos import Point


class ProductList(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        create user in temp database to test the api
        """
        address = Address.objects.create(location=Point(0.0, 0.0), address_info='talkha-mansora', city='mansoura')
        user = User.objects.create(user_name='omar', password=make_password('123456'), address=address)
        User.objects.create_token(user)
        item = Item.objects.create(price=210, is_available=True, title='gum', description='mango flavored gum')
        city = City.objects.create(name='mansoura')
        branch = Branch.objects.create(name='talkha', cities=city)
        BranchItem.objects.create(branch=branch, item=item, is_available=True, branch_item_price=190)

    def test_product_list_api(self):
        url = "/api/product/"

        user_token = User.objects.first().token
        headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + user_token
        }
        response = self.client.get(url, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


