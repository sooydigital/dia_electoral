from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class Command(BaseCommand):
    def handle(self, *args, **options):
        users = [
            {
                'username': "Yurs",
                'first_name': "Yurley",
                'last_name': "Sanchez",
                'password': "admin",
                'role': "SUPER_ADMIN",
            },
            {
                'username': "Macghan",
                'first_name': "Mac",
                'last_name': "Herrera",
                'password': "Macghan31*",
                'role': "SUPER_ADMIN",
            },
        ]

        for user in users:
            role = user.get('role')
            grupo = Group.objects.get(name=role)

            if not User.objects.filter(email=user['username']).exists():
                print(">>> User with username: '{}' created".format(user['username']))
                user_object = User(username=user['username'], email=user['username'], first_name=user['first_name'],
                                   last_name=user['last_name'])
                user_object.set_password(user['password'])
                user_object.save()
                user_object.groups.add(grupo)
                user_object.is_staff = True
                user_object.save()


        if not User.objects.filter(email='admin@mail.com').exists():
            user_object = User(username='admin', email='admin@mail.com', first_name='admin', last_name="super")
            user_object.set_password('admin')
            user_object.is_superuser = True
            user_object.is_staff = True

            user_object.save()

            print(">>> User with username: '{}' created".format('admin'))