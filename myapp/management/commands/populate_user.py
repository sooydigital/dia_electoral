from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

TESTIGOS = '''CEDULA;Nombre
4164585382;John Turford
4030980732;Horst Rossander
807051233;Shanna Bedrosian
5385988308;Fina Rumgay
1074724208;Kaja Comsty
7697613158;Jefferson Auger
2923644395;Clayson Twittey
6106828881;Shelba Craine
3180279001;Clareta Wimbury
7687367421;Janey Valek
4904627377;Milty Tant
1832068005;Sean McGonigle
560510357;Denis Barrable
1838241280;Neysa Heatley
6406966589;Amby Harder
415205808;Franciskus Upsale
2357434236;Anestassia Sainthill
4017774504;Vinnie Brydson
6066929798;Patrizio Mauser
9679903486;Valerie Pladen
1146276923;Pamela Perkin
5940357393;Nichole Lansdowne
5876262196;Morissa Abel
9346051183;Randell McGavin
404356680;Anabella Medgewick
9755469214;Wendall Durtnel
8068103678;Standford Ionesco
2886893129;Angelica Barthod
7208332061;Ly Wilkie'''

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

        if TESTIGOS:
            testigos = TESTIGOS.split('\n')

            grupo_testigo = Group.objects.get(name='TESTIGO')
            for testigo in testigos:
                data = testigo.split(';')
                document_id = data[0]
                nombre = data[1]
                fake_email = '{}@mail.com'.format(document_id)
                if not User.objects.filter(email=fake_email).exists():
                    user_object = User(username=document_id, email=fake_email, first_name=nombre, last_name="")
                    user_object.set_password(document_id)
                    # user_object.groups.add(grupo_testigo)
                    user_object.save()

                    print(">>> User with document id: '{}' created".format(document_id))