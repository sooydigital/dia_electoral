from myapp.models import PuestoVotacion, Mesa, Registro, Candidato
from django.contrib.auth.models import User

from django.core.management.base import BaseCommand

DISTRIBUCION = '''
4164585382;IE MAIPORÉ SEDE B;1 2 3 4
4030980732;IE MAIPORÉ SEDE B;5 6 7 8
807051233;IE MAIPORÉ SEDE B;9 10
5385988308;IE MAIPORÉ SEDE B;11 12 13
1074724208;IE MAIPORÉ SEDE B;14 15
7697613158;IE MAIPORÉ SEDE B;16 17
2923644395;IE MAIPORÉ SEDE B;18 19 20 21
6106828881;IE MAIPORÉ SEDE B;22 23 24 25 26
3180279001;ORDEN DE LOS CLÉRIGOS REG SOMASCOS;1 2 3 4
7687367421;ORDEN DE LOS CLÉRIGOS REG SOMASCOS;5 6 7 8
4904627377;ORDEN DE LOS CLÉRIGOS REG SOMASCOS;9 10 11
1832068005;ORDEN DE LOS CLÉRIGOS REG SOMASCOS;12 13
560510357;ORDEN DE LOS CLÉRIGOS REG SOMASCOS;14 15
1838241280;ORDEN DE LOS CLÉRIGOS REG SOMASCOS;16 17
415205808;ORDEN DE LOS CLÉRIGOS REG SOMASCOS;18 19 20 21
2357434236;ORDEN DE LOS CLÉRIGOS REG SOMASCOS;22 23 24 25 26
4017774504;COLEGIO FE Y ALEGRIA LOS COLORADOS;1 2
6066929798;COLEGIO FE Y ALEGRIA LOS COLORADOS;3 4 5
9679903486;COLEGIO FE Y ALEGRIA LOS COLORADOS;6 7
1146276923;COLEGIO FE Y ALEGRIA LOS COLORADOS;8 9 
5940357393;COLEGIO FE Y ALEGRIA LOS COLORADOS;10 11
5876262196;COLEGIO FE Y ALEGRIA LOS COLORADOS;12 13 14
9346051183;COLEGIO FE Y ALEGRIA LOS COLORADOS;15 16 17
404356680;IE RURAL BOSCONIA;1
9755469214;IE RURAL BOSCONIA;2
8068103678;IE RURAL BOSCONIA;3
2886893129;IE RURAL BOSCONIA;4
7208332061;IE RURAL BOSCONIA;5
8079530653;IE RURAL BOSCONIA;6
8852968458;IE CAFÉ MADRID;1 2
8952423704;IE CAFÉ MADRID;3 4
7268398204;IE CAFÉ MADRID;5 6
4878196106;IE CAFÉ MADRID;7 8
4937871366;IE CAFÉ MADRID;9 10
8558814775;IE CAFÉ MADRID;11 12
7116440151;IE CAFÉ MADRID;13 14
7509572924;IE CAFÉ MADRID;15 16
6502220908;IE RURAL BOSCONIA;1 2 3
4916000730;I.E. LA JUVENTUD SEDE A;1 2 3
8161884242;UNIVERSIDAD INDUSTRIAL DE SANTANDER;1 2 3
1860661718;COL FRANCISCANO DEL VIRREY SOL;1 2 3
2105986005;IE MAIPORÉ SEDE B;1 2 3
9444949621;IE TEC RAFAEL GARCIA HERREROS;1 2 3
6224997535;IE CAFÉ MADRID;1 2 3
9495452430;COLEGIO FE Y ALEGRIA LOS COLORADOS;1 2 3
9170105987;SALON COMUNAL EL PABLON;1 2 3
8486930634;CENTRO VIDA KENNEDY;1 2 3
1579357210;I.E. SANTO ANGEL;1 2 3
368613356;INST DE PROM SOC DEL NORTE SEDE A;1 2 3
5772419684;ORDEN DE LOS CLÉRIGOS REG SOMASCOS;1 2 3
4246348473;IE DÁMASO ZAPATA SEDE C;1 2 3
202956970;IE RURAL BOSCONIA;1 2 3
9686580077;I.E. LA JUVENTUD SEDE A;1 2 3
1461192706;UNIVERSIDAD INDUSTRIAL DE SANTANDER;1 2 3
8095691208;COL FRANCISCANO DEL VIRREY SOL;1 2 3
2127676637;IE MAIPORÉ SEDE B;1 2 3
3253469417;IE TEC RAFAEL GARCIA HERREROS;1 2 3
1786665573;IE CAFÉ MADRID;1 2 3
1322274517;COLEGIO FE Y ALEGRIA LOS COLORADOS;1 2 3
4541489031;SALON COMUNAL EL PABLON;1 2 3
2639031945;CENTRO VIDA KENNEDY;1 2 3
9371981539;I.E. SANTO ANGEL;1 2 3
7399556423;INST DE PROM SOC DEL NORTE SEDE A;1 2 3
2834747466;ORDEN DE LOS CLÉRIGOS REG SOMASCOS;1 2 3
7417031277;IE DÁMASO ZAPATA SEDE C;1 2 3
4020418136;IE RURAL BOSCONIA;1 2 3
4151720278;I.E. LA JUVENTUD SEDE A;1 2 3
4850074413;UNIVERSIDAD INDUSTRIAL DE SANTANDER;1 2 3
63039117;COL FRANCISCANO DEL VIRREY SOL;1 2 3'''


class Command(BaseCommand):
    def handle(self, *args, **options):

        if DISTRIBUCION:
            distribuciones = DISTRIBUCION.split('\n')
            canditatos = Candidato.objects.all()
            for distribucion in distribuciones:
                data = distribucion.split(';')
                if len(data)>1:
                    document_id = data[0]
                    nombre = data[1]
                    mesas_str = data[2]
                    mesas = mesas_str.split(' ')

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

                    for mesa in mesas:
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

                               
                        
