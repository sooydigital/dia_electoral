from django.core.management.base import BaseCommand
from myapp.models import Municipio, Barrio, Departamento, Comuna

class Command(BaseCommand):
    def handle(self, *args, **options):
        locations = {
            "BUCARAMANGA": {
                "COMUNA 01": [
                    "KENNEDY",
                    "TEJAR NORTE",
                    "BETANIA",
                    "CAFÉ MADRID",
                    "MINUTO DE DIOS",
                    "COLORADOS",
                    "VILLA ROSA",
                ],
                "COMUNA 02": [
                    "SAN CRISTOBAL",
                    "REGADERO",
                    "VILLA HELENA",
                    "BOSCONIA",
                    "LA JUVENTUD",
                    "TRANSICION 1",
                    "TRANSICION 3",
                    "TRANSICION 5",
                    "LA INDEPENDENCIA",
                    "ESPERANZA 1",
                    "ESPERANZA 2",
                    "ESPERANZA 3",
                ],
                "COMUNA 03": [
                    "LA UNIVERSIDAD",
                    "SAN FRANCISCO ",
                    "COMUNEROS",
                    "MUTUALIDAD",
                    "SAN RAFAEL",
                ],
                "COMUNA 04": [
                    "GIRATDOT",
                    "GAITÁN",
                    "SANTANDER",
                    "LA FERIA",
                    "GRANADA",
                ],
                "COMUNA 05": [
                    "LA JOYA",
                    "CAMPO HERMOSO",
                    "ALFONSO LÓPEZ",
                ],
                "COMUNA 06": [
                    "LA CONCORDIA",
                    "LA VICTORIA",
                    "SAN MIGUEL",
                    "RICAURTE",
                ],
                "COMUNA 07": [
                    "CIUDADELA REAL DE MINAS",
                ],
                "COMUNA 08": [
                    "LOS CANELOS",
                    "PABLO VI",
                    "BUCARAMANGA",
                ],
                "COMUNA 09": [
                    "LA LIBERTAD",
                    "SAN MARTIN",
                ],
                "COMUNA 10": [
                    "PROVENZA",
                    "DIAMANTE II",
                    "SAN LUIS"
                    "FONTANA",
                ],
                "COMUNA 11": [
                    "EL PORVENIR",
                    "DELICIAS ALTAS",
                    "MANUELA BELTRÁN",
                    "EL ROCIO",
                    "DANGOND",
                    "TOLEDO PLATA",
                ],
                "COMUNA 12": [
                    "NUEVO SOTOMAYOR",
                    "CONUCOS",
                    "EL JARDIN",
                    "SOTOMAYOR",
                    "CABECERA DEL LLANO",
                    "TERRAZAS",
                    "LA FLORESTA",
                    "PAN DE AZUCAR",
                ],
                "COMUNA 13": [
                    "SAN ALONSO",
                    "ALARCON",
                    "LA AURORA",
                    "ALVAREZ",
                    "BOLIVAR",
                    "ANTONIA SANTOS",
                    "MEJORAS PUBLICAS",
                    "EL PRADO",
                ],
                "COMUNA 14": [
                    "ALBANIA",
                    "MIRAFLORES",
                    "MORRORICO",
                    "BUENOS AIRES",
                ],
                "COMUNA 15": [
                    "GARCIA ROVIRA",
                    "EL CENTRO",
                ],
                "COMUNA 16": [
                    "EL TEJAR",
                    "QUINTAS DEL CACIQUE",
                    "SANTA BARBARA",
                    "UDES",
                    "LAGOS DEL CACIQUE",
                ],
                "COMUNA 17": [
                    "MUTIS",
                    "ESTORAQUES",
                    "MONTERREDONDO",
                ],
            },
            # "FLORIDABLANCA": {
            #     "ALTAMIRA Y CASCO ANTIGUO": [
            #         "FLORIDA CENTRO",
            #          "JARDIN DE LIMONCITO",
            #          "LIMONCITO ",
            #          "ALTAMIRA",
            #          "VILLAS DE SAN FCO ",
            #          "VILLA PIEDRA DEL SOL ",
            #          "LA PAZ",
            #     ],
            #     "CAÑAVERAL": [
            #         "CAÑAVERAL",
            #     ],
            #     "BUCARICA": [
            #         "BUCARICA",
            #         "SIMON BOLIVAR",
            #         "CARACOLI",
            #     ],
            #     "CALDAS Y REPOSO": [
            #         "CALDAS",
            #         "SAN BERNARDO",
            #         "VILLALUZ",
            #         "LAURELES",
            #         "EL DORADO",
            #         "HACIENDA SAN JUAN ",
            #         "ALTOVIENTO 1,2",
            #         "ZAPAMANGA 1,2,3,4,5,6,7",
            #     ],
            #     "BOSQUE MOLINOS": [
            #         "BOSQUE ",
            #         "MOLINOS",
            #         "NIZA",
            #         "VILLA ESPAÑA",
            #         "PALOMITAS",
            #         "PARQUE SAN AGUSTIN ",
            #         "VILLAS DE MEDITERRANEO",
            #     ],
            #     "LAGOS-BELLAVISTA": [
            #         "LAGOS 1, 2,3,4 Y 5",
            #         "BELLAVISTA",
            #         "ALTOS DE BELLAVISTA",
            #     ],
            #     "CIUDAD VALENCIA-SANTANA": [
            #         "CIUDAD VALENCIA",
            #         "SANTANA ",
            #         "ROSALES",
            #         "PRADOS DEL SUR",
            #         "GUANATA",
            #     ],
            #     "CUMBRE-CARMEN ": [
            #         "EL CARMEN 1, 2, 3, 4",
            #         "VILLA ALCAZAR",
            #         "LA CUMBRE",
            #         "GARCIA ECHEVERRY ",
            #         "SURATOQUE ",
            #     ]
            # },
            # "GIRON": {
            #     "Giron": [
            #         'RIBERA DEL RIO',
            #         'VILLA DE LOS CABALLEROS',
            #         'VIDA EN PRIMAVERA',
            #         'VILLAS DE SAN JUAN',
            #         'ALDEA MEDIA',
            #         'BELLAVISTA',
            #         'BRISAS DEL RIO',
            #         'EL CARMEN',
            #         'EL PROGRESO',
            #         'ESPAÑA',
            #         'LOS BAMBUES',
            #         'MALPASO',
            #         'CIUDADELA NUEVO GIRON',
            #         'PUEBLITO VIEJO',
            #         'ALDEA ALTA',
            #         'ARENALES CAMPESTRE',
            #         'BALCONES DEL PORTAL',
            #         'CORVIANDI 1 Y 3',
            #         'ELOY VALENZUELA',
            #         'ESPAÑA',
            #         'LA ESMERALDA',
            #         'LOS CAMBULOS',
            #         'MIRADOR DE ARENALES',
            #         'PALENQUE',
            #         'RIO PRADO',
            #         'SAN ANTONIO CARRIZAL',
            #         'VALLE DE LOS CABALLEROS',
            #         'VILLA EVA',
            #         'VILLA LINDA',
            #         'ALTOS DE ARENALES',
            #         'APARTAMENTOS CARRIZAL',
            #         'LA CAMPIÑA',
            #         'CARRIZAL CAMPESTRE',
            #         'GIRON CENTRO',
            #         'CASTILLA REAL UNO',
            #         'EL GALLINERAL',
            #         'EL LLANITO',
            #         'EL POBLADO',
            #         'EL TEJAR',
            #         'VILLAMIL',
            #         'PUERTO MADERO',
            #         'GIRALUZ',
            #         'POBLADO',
            #         'LA RINCONADA',
            #         'RINCON DE GIRON ',
            #         'PORTAL CAMPESTRE NORTE 1, 2, 3 Y 4',
            #         'SANTA CRUZ',
            #         'VILLA CAMPESTRE',
            #         'ALICANTE',
            #         'CASTILLA LA NUEVA',
            #         'LA ARBOLEDA',
            #         'ALICANTE',
            #     ]
            # },
            # "PIEDECUESTA": {
            #     "Piedecuesta": [
            #         "SECTOR EL EDEN",
            #         "SECTOR EL EDEN DOS",
            #         "SECTOR MATA DE CAÑA",
            #         "BRISAS DE PRIMAVERA 1 y 2",
            #         "LOS CISNES ",
            #         "SAN JUAN",
            #         "GRANADILLO",
            #         "REFUGIO",
            #         "PORTAL DEL TALAO CASAS",
            #         "PAISANDU",
            #         "TEJADITOS",
            #         "PORTAL DEL VALLE",
            #         "PORTAL DEL VALLE",
            #         "CABECERA",
            #         "LA COLINA",
            #         "SAN CARLOS",
            #         "CAMPO VERDE",
            #         "CHACARITA",
            #         "BARILOCHE",
            #         "BUENOS AIRES",
            #         "PORTAL DEL TALAO CASAS Y APTOS",
            #         "VILLA NUEVA",
            #         "HOYO CHIQUITO",
            #         "HOYO GRANDE",
            #         "SURATOQUE",
            #         "LA FERIA",
            #         "TEJADITOS",
            #         "LA ARGENTINA",
            #         "SAN TELMO UNO",
            #         "SAN TELMO DOS",
            #         "JUNIN CASAS",
            #         "LA RIOJA",
            #         "VILLA SOFIA",
            #         "ARBORETO APARTAMENTO",
            #         "ENTREPARQUES APARTAME",
            #         "SANTILLANA CONJUNTO",
            #         "TORRES DE UMPLALA APART.",
            #         "VILLA MARCELA II APART.",
            #         "PALCO DE BARRO BLANCO APAR",
            #         "MIRAFLORES APARTAMENTO",
            #         "PASEO DEL PUENTE UNO",
            #         "PASEO DEL PUENTE DOS",
            #         "PASEO REAL APARTAMENTOS UNO",
            #         "PASEO REAL APARTAMENTOS DOS",
            #         "BOSQUES DE PIEDECUESTA",
            #         "MOLINOS DE VIENTO",
            #         "SAN CRISTOBAL",
            #         "CONJUNTO MONTE REAL",
            #         "SAN FRANCISCO",
            #         "PALERMO UNO Y DOS",
            #         "CATALUÑA",
            #         "VILLA NAVARRA",
            #         "SAN RAFAEL",
            #         "SAN ANTONIO",
            #         "CENTRO",
            #         "LA CANDELARIA",
            #         "LA NUEVA CANDELARIA",
            #         "CALLEJUELAS APARTAMENTOS",
            #         "MOLINO VIENTOS CONJU CERRAD",
            #         "QUINTA GRANADA Y ALTOS DE GRANADA",
            #         "PINARES CAMPESTRE, CONDOMINIO CLUB, NUEVO PINARESS",
            #     ]
            # },
            # "LEBRIJA": {
            #     "Lebrija": [
            #         "SANTA BARBARA",
            #         "LA LOMA",
            #         "VILLA CLAUDIA",
            #         "EL CHIRILI BRISAS N.AMAN",
            #         "VILLA ESPERANZA",
            #         "LOS PINOS",
            #         "MARIA PAZ",
            #         "CAMPESTRE REAL",
            #         "CAMPO ALEGRE",
            #         "SAN DIEGO",
            #         "BRISAS DE CAMPO ALEGRE",
            #         "EL PESEBRE",
            #         "CIUDADELA DEL RIO",
            #         "SAN JORGE",
            #         "LAURELES",
            #         "ESMERALDA",
            #         "LOS ROSALES",
            #         "EL PRADO",
            #         "ASOVICOL",
            #         "LA POPA",
            #         "VILLA PARAISO",
            #         "LA CIUDADELA RIOS CORTEZ",
            #         "CENTRO"
            #     ]
            # },
        }

        departamento_name = 'SANTANDER'
        departamento_object = None

        if not Departamento.objects.filter(name=departamento_name).exists():
            departamento_object = Departamento(name=departamento_name)
            departamento_object.save()

        else:
            departamento_object = Departamento.objects.filter(name=departamento_name).first()

        for municipio, comunas in locations.items():
            # create municipo
            municipio_object = None
            if not Municipio.objects.filter(name=municipio, departamento__name=departamento_name).exists():
                print(">>> Municipio with label: '{}' created".format(municipio))
                municipio_object = Municipio(name=municipio, departamento=departamento_object)
                municipio_object.save()
            else:
                municipio_object = Municipio.objects.filter(name=municipio).first()

            for comuna, barrios in comunas.items():
                if not Comuna.objects.filter(name=comuna, municipio__name=municipio).exists():
                    print(">>>>> Comuna with label: '{}' created".format(comuna))
                    comuna_object = Comuna(municipio=municipio_object, name=comuna)
                    comuna_object.save()
                else:
                    comuna_object = Comuna.objects.filter(municipio__name=municipio, name=comuna).first()

                for barrio in barrios:
                    if not Barrio.objects.filter(name=barrio, comuna__name=comuna, municipio__name=municipio).exists():
                        print(">>>>> Barrio with label: '{}' created".format(barrio))
                        barrio_object = Barrio(municipio=municipio_object, comuna=comuna_object, name=barrio)
                        barrio_object.save()