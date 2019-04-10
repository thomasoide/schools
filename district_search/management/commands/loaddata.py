"""Load raw RMP data from source files into models."""
import os
from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import DataError
from district_search.models import Districts
from schools.settings import DATA_DIR
from os import listdir
from os.path import isfile, join
import logging
from django.core.management import call_command


class Command(BaseCommand):
    """
    Load district data into PostgreSQL database
    """

    def handle(self, *args, **kwargs):
        self.stdout.write('Flushing data...', ending='')
        management.call_command(
            'flush', verbosity=0, interactive=False,
        )
        self.stdout.write(
            self.style.SUCCESS('OK')
        )
        insert_count = Districts.objects.from_csv(os.path.join(DATA_DIR, 'districts.csv'))
        print("{} records inserted".format(insert_count))
