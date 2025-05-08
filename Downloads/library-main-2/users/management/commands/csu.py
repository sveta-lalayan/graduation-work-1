
from django.core.management import BaseCommand

from users.models import Users


class Command(BaseCommand):
    def handle(self, *args, **options):
        user, created = Users.objects.get_or_create(email="123@yandex.ru")
        user.set_password("123qwe")
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()