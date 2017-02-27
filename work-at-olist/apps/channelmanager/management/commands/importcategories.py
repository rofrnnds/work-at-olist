from django.core.management.base import BaseCommand
from apps.channelmanager.models import Category, Channel
import csv


class Command(BaseCommand):
    help = 'Import categories from a CSV file to a given channel.'

    def add_arguments(self, parser):
        parser.add_argument('channel', type=str)
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        channel_name = options['channel']
        channel, created = Channel.objects.get_or_create(name=channel_name)
        print('Importing Categories...')
        with open(options['csv_file']) as csv_file:
            for row in csv.DictReader(csv_file):
                categories = row['Category'].split(' / ')
                parent = None
                for category_name in categories:
                    category, created = Category.objects.update_or_create(
                        name=category_name, channel=channel, parent=parent)
                    parent = category

        print('Categories imported!')
