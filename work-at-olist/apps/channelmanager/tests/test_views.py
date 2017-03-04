from rest_framework.test import APITestCase
from apps.channelmanager.models import Channel, Category
from rest_framework.reverse import reverse


class ChannelAPITest(APITestCase):

    def setUp(self):
        self.test_channel = Channel.objects.create(name='wallmart')

        Channel.objects.create(name='americanas')
        Channel.objects.create(name='amazon')

        self.response_list = self.client.get(reverse('channels-api-list'),
                                             format='json').json()
        self.response_detail = self.client.get(
            reverse('channels-api-detail',
                    args=[str(self.test_channel.slug)]), format='json').json()

    def test_list(self):
        self.assertEquals(self.response_list[0]['name'], 'wallmart')
        self.assertEquals(self.response_list[1]['name'], 'americanas')
        self.assertEquals(self.response_list[2]['name'], 'amazon')

    def test_retrieve(self):
        self.assertEqual(self.response_detail['slug'], self.test_channel.slug)
        self.assertEqual(self.response_detail['name'], self.test_channel.name)

    def test_list_hyperlink(self):
        hyperlink_response = self.client.get(self.response_list[0]['url'])
        self.assertEqual(hyperlink_response.status_code, 200)

    def test_detail_hyperlink(self):
        hyperlink_response = self.client.get(self.response_detail['url'])
        self.assertEqual(hyperlink_response.status_code, 200)

    def test_channel_id_is_not_exposed_in_API(self):
        self.assertNotIn(str(self.test_channel.id), str(self.response_list))
        self.assertNotIn(str(self.test_channel.id), str(self.response_detail))


class CategoryAPITest(APITestCase):

    def setUp(self):
        self.test_channel = Channel.objects.create(name='wallmart')
        self.test_category = Category.objects.create(channel=self.test_channel,
                                                     name='Games')
        self.test_subcategory = Category.objects.create(
            channel=self.test_channel, name='XBOX 360',
            parent=self.test_category)
        self.test_subsubcategory = Category.objects.create(
            channel=self.test_channel, name='Accessories',
            parent=self.test_subcategory)
        self.response_list = self.client.get(reverse('categories-api-list'),
                                             format='json').json()
        self.response_detail = self.client.get(
            reverse('categories-api-detail',
                    args=[str(self.test_category.slug)]), format='json').json()

    def test_list(self):
        self.assertEquals(self.response_list[0]['name'], 'Games')
        self.assertEquals(self.response_list[1]['name'], 'XBOX 360')

    def test_retrieve(self):
        self.assertEqual(self.response_detail['slug'],
                         self.test_category.slug)
        self.assertEqual(self.response_detail['name'], self.test_category.name)

    def test_list_hyperlink(self):
        hyperlink_response = self.client.get(self.response_list[0]['url'])
        self.assertEqual(hyperlink_response.status_code, 200)

    def test_detail_hyperlink(self):
        hyperlink_response = self.client.get(self.response_detail['url'])
        self.assertEqual(hyperlink_response.status_code, 200)

    def test_retrieve_with_parent_and_children(self):
        self.assertEqual(self.response_detail['parent'],
                         self.test_category.parent)
        self.assertEqual(self.response_detail['children'][0]['name'],
                         self.test_subcategory.name)
        self.assertEqual(
            self.response_detail['children'][0]['children'][0]['name'],
            self.test_subsubcategory.name)

    def test_category_id_is_not_exposed_in_API(self):
        self.assertNotIn(str(self.test_category.id), str(self.response_list))
        self.assertNotIn(str(self.test_category.id), str(self.response_detail))
