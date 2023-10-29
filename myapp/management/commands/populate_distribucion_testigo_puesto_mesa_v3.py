from myapp.models import PuestoVotacion, Mesa, Registro, Candidato
from django.contrib.auth.models import User

from django.core.management.base import BaseCommand

DISTRIBUCION = '''1052836585;COL NUESTRA SEÑORA DEL ROSARIO;1
1052836585;COL NUESTRA SEÑORA DEL ROSARIO;2
1052836585;COL NUESTRA SEÑORA DEL ROSARIO;3
1052836585;COL NUESTRA SEÑORA DEL ROSARIO;4
1082832188;COL NUESTRA SEÑORA DEL ROSARIO;5
1082832188;COL NUESTRA SEÑORA DEL ROSARIO;6
1082832188;COL NUESTRA SEÑORA DEL ROSARIO;7
1082832188;COL NUESTRA SEÑORA DEL ROSARIO;8'''


class Command(BaseCommand):
    def handle(self, *args, **options):

        if DISTRIBUCION:
            distribuciones = DISTRIBUCION.split('\n')
            canditatos = Candidato.objects.all()
            for distribucion in distribuciones:
                data = distribucion.split(';')
                if len(data)>2:
                    document_id = data[0]
                    nombre = data[1]
                    mesa = data[2]

                    if not PuestoVotacion.objects.filter(
                        nombre=nombre,
                    ).exists():
                        print(">>> este puesto de votacion no esta creado: '{}'".format(nombre))
                        continue

                    puesto_votacion_obj = PuestoVotacion.objects.filter(
                        nombre=nombre,
                    ).first()

                    if not User.objects.filter(username=document_id).exists():
                        print(">>> este usuario no esta creado: '{}'".format(document_id))
                        continue

                    user_obj = User.objects.filter(
                        username=document_id,
                    ).first()

                    if not mesa:
                        continue

                    if not Mesa.objects.filter(puesto_votacion=puesto_votacion_obj, numero=mesa).exists():
                        mesa_object = Mesa(puesto_votacion=puesto_votacion_obj, numero=mesa)
                        mesa_object.save()

                    else:
                        mesa_object = Mesa.objects.filter(puesto_votacion=puesto_votacion_obj, numero=mesa).first()

                    for canditato in canditatos:
                        print(user_obj, mesa_object, canditato)

                        if not Registro.objects.filter(testigo=user_obj, mesa=mesa_object, candidato=canditato).exists():
                            registro_object = Registro(testigo=user_obj, mesa=mesa_object, candidato=canditato)
                            registro_object.save()
