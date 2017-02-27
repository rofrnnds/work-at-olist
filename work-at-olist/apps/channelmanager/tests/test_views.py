from rest_framework.test import APITestCase
from apps.channelmanager.models import Channel, Category
from rest_framework.reverse import reverse


class ChannelAPITest(APITestCase):

    def setUp(self):
        self.test_channel = Channel.objects.create(name='wallmart')
        Channel.objects.create(name='americanas')
        Channel.objects.create(name='amazon')

    def test_list(self):
        url = reverse('channels-api-list')
        response = self.client.get(url, format='json').json()
        self.assertEquals(response[0]['name'], 'wallmart')
        self.assertEquals(response[1]['name'], 'americanas')
        self.assertEquals(response[2]['name'], 'amazon')

    def test_retrieve(self):
        url = reverse('channels-api-detail', args=[str(self.test_channel.id)])
        response = self.client.get(url, format='json').json()
        channel = Channel.objects.get(id=self.test_channel.id)
        self.assertEqual(response['id'], str(channel.id))
        self.assertEqual(response['name'], channel.name)


class CategoryAPITest(APITestCase):

    def setUp(self):
        self.test_channel = Channel.objects.create(name='wallmart')
        self.test_category = Category.objects.create(channel=self.test_channel,
                                                     name='Games')
        self.test_subcategory = Category.objects.create(
            channel=self.test_channel,
            name='XBOX 360',
            parent=self.test_category)

    def test_list(self):
        url = reverse('categories-api-list')
        response = self.client.get(url, format='json').json()
        self.assertEquals(response[0]['name'], 'Games')
        self.assertEquals(response[1]['name'], 'XBOX 360')

    def test_retrieve(self):
        url = reverse('categories-api-detail',
                      args=[str(self.test_category.id)])
        response = self.client.get(url, format='json').json()
        category = Category.objects.get(id=self.test_category.id)
        self.assertEqual(response['parent'], category.parent)
        self.assertEqual(response['id'], str(self.test_category.id))
        self.assertEqual(response['name'], self.test_category.name)
        self.assertEqual(response['children'][0]['name'],
                         self.test_subcategory.name)
