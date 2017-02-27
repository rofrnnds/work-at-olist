from django.test import TestCase
from apps.channelmanager.models import Channel, Category
from django.db.models import UUIDField


class ChannelModelTest(TestCase):

    def setUp(self):
        self.channels_name = "a testing channel"
        self.channel = Channel.objects.create(name=self.channels_name)

    def test_channel_was_created_with_a_name(self):
        channel = Channel.objects.get(name=self.channels_name)
        self.assertEqual(self.channel.name, channel.name)

    def test_channel_model_has_a_unique_identifier_field(self):
        self.assertTrue(isinstance(Channel._meta.get_field("id"), UUIDField))


class CategoryModelTest(TestCase):

    def setUp(self):
        self.categorys_name = "a testing category"
        self.channel = Channel.objects.create(name="a testing channel")
        self.category = Category.objects.create(
            name=self.categorys_name, channel=self.channel)

    def test_category_was_created_with_a_name(self):
        category = Category.objects.get(name=self.categorys_name)
        self.assertEqual(self.category.name, category.name)

    def test_channel_model_has_a_unique_identifier_field(self):
        self.assertTrue(isinstance(Channel._meta.get_field("id"), UUIDField))

    def test_can_add_another_category_as_sub_category(self):
        self.subcategory = Category.objects.create(
            name="a testing sub-category", channel=self.channel,
            parent=self.category)
        self.assertIsNotNone(self.subcategory.parent)
