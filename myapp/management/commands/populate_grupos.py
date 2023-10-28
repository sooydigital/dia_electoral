from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

ALL_GROUP = ['SUPER_ADMIN', 'TESTIGO']


class Command(BaseCommand):
    def handle(self, *args, **options):
        for group in ALL_GROUP:
            if not Group.objects.filter(name=group).exists():
                Group.objects.create(name=group)
