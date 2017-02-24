from django.test import TestCase
from .models import Channel


class TestChannel(TestCase):

    def setUp(self):
        self.channels_name = "a testing channel"
        self.channel = Channel.objects.create(name=self.channels_name)

    def test_can_create_a_channel(self):
        self.assertIsNotNone(self.channel)

    def test_channel_was_created_with_a_name(self):
        self.assertEqual(self.channel.name, self.channels_name)
