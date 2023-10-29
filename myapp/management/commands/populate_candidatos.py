from myapp.models import Candidato
from django.core.management.base import BaseCommand

CANDIDATOS = '''Candidatura	Nombre
Alcaldía;Carlos Sotomonte
Alcaldía;Jaime Beltran
Gobernación;Juvenal Díaz
Gobernación;Hector Mantilla
Concejo;A1
Concejo;B2
Concejo;C3
Asamblea;D1
Asamblea;E2'''


class Command(BaseCommand):
    def handle(self, *args, **options):

        if CANDIDATOS:
            candidatos = CANDIDATOS.split('\n')

            for candidato in candidatos:
                data = candidato.split(';')
                if len(data)>1:
                    candidatura = data[0]
                    nombre = data[1]
                    if not Candidato.objects.filter(candidatura=candidatura, nombre=nombre).exists():
                        candidato_obj = Candidato(candidatura=candidatura, nombre=nombre)
                        candidato_obj.save()
                        print(">>> candidato: '{}' created".format(candidato))