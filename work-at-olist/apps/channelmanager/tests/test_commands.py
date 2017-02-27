from django.test import TestCase
from django.core import management
from apps.channelmanager.models import Channel, Category
import os


class ImportCategoriesCommandTest(TestCase):

    def setUp(self):
        self.csv_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'fixtures.csv')

    def test_command_create_a_channel(self):
        self.assertEquals(Channel.objects.filter(name='walmart').count(), 0)
        management.call_command('importcategories', 'walmart', self.csv_file)
        self.assertEquals(Channel.objects.filter(name='walmart').count(), 1)

    def test_command_overwrites_existing_channel(self):
        management.call_command('importcategories', 'walmart', self.csv_file)
        management.call_command('importcategories', 'walmart', self.csv_file)
        self.assertEquals(Channel.objects.filter(name='walmart').count(), 1)

    def test_command_import_all_fixture_data(self):
        management.call_command('importcategories', 'walmart', self.csv_file)
        self.assertEquals(Category.objects.all().count(), 23)

    def test_categories_relationship(self):
        management.call_command('importcategories', 'walmart', self.csv_file)
        # Books / National Literature / Science Fiction
        self.assertEquals(Category.objects.filter(
            name='Science Fiction',
            parent__name='National Literature',
            parent__parent__name='Books').count(), 1)
