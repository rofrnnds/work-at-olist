from django.test import TestCase
from apps.channelmanager.models import Channel, Category


class TestChannel(TestCase):

    def setUp(self):
        self.channels_name = "a testing channel"
        self.channel = Channel.objects.create(id=1, name=self.channels_name)

    def test_channel_was_created(self):
        channel = Channel.objects.get(id=1)
        self.assertIsNotNone(channel)

    def test_channel_was_created_with_a_name(self):
        self.assertEqual(self.channel.name, self.channels_name)


class TestCategory(TestCase):

    def setUp(self):
        self.categorys_name = "a testing category"
        self.channel = Channel.objects.create(id=1, name="a testing channel")
        self.category = Category.objects.create(
            id=1, name=self.categorys_name, channel=self.channel)

    def test_category_was_created(self):
        category = Category.objects.get(id=1)
        self.assertIsNotNone(category)

    def test_category_was_created_with_a_name(self):
        self.assertEqual(self.category.name, self.categorys_name)

    def test_can_add_another_category_as_sub_category(self):
        self.subcategory = Category.objects.create(
            name="a testing sub-category", channel=self.channel,
            parent=self.category)
        self.assertIsNotNone(self.subcategory.parent)