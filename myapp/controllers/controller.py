from myapp.models import Registro
from django.db.models import Count
from django.db.models import Sum


class Controller():

    @staticmethod
    def get_mesas_by_user(user):
        query = Registro.objects.filter(testigo=user)
        if query.exists():
            mesas = list(query.values('mesa__numero', 'mesa__id', 'mesa__puesto_votacion__nombre').distinct())
            return mesas
        else:
            return []

    @staticmethod
    def get_distribucion_by_mesa_and_user(user, mesa_id):
        query = Registro.objects.filter(testigo=user, mesa_id=mesa_id)
        if query.exists():
            distribucion = list(query.values('id', 'candidato__candidatura', 'candidato__nombre', 'numero_de_votos'))

            result_dict = {}

            for item in distribucion:
                candidatura = item.get("candidato__candidatura")
                if candidatura not in result_dict:
                    result_dict[candidatura] = [[str(item.get("id")), item.get("candidato__nombre"), item.get('numero_de_votos')]]
                else:
                    result_dict[candidatura].append([str(item.get("id")), item.get("candidato__nombre"), item.get('numero_de_votos')])

            return result_dict
        else:
            return {}

    @staticmethod
    def actualiza_registro(uuid_obj, data):
        registro = Registro.objects.get(id=uuid_obj)
        valor = data.get('valor')
        if not valor:
            return None
        valor = valor.replace('.', "")
        if valor.isnumeric():
            registro.numero_de_votos = valor
            registro.save()

    @staticmethod
    def get_structure(user):

        data = [
            {
                'mesa': 1,
                'data': [
                    {
                        'candidatura': 'Alcaldía',
                        'candidato_id': '1',
                        'candidato_name': 'Carlos Sotomonte',
                        'registro_id': '12'
                    },
                    {
                        'candidatura': 'Alcaldía',
                        'candidato_id': '2',
                        'candidato_name': 'Jaime Beltran',
                        'registro_id': '13'
                    },
                    {
                        'candidatura': 'Gobernación',
                        'candidato_id': '3',
                        'candidato_name': 'Juvenal Díaz',
                        'registro_id': '14'
                    },
                    {
                        'candidatura': 'Gobernación',
                        'candidato_id': '3',
                        'candidato_name': 'Hector Mantilla',
                        'registro_id': '14'
                    }
                ]

            },
            {
                'mesa': 2,
                'data': [
                    {
                        'candidatura': 'Alcaldía',
                        'candidato_id': '1',
                        'candidato_name': 'Carlos Sotomonte',
                        'registro_id': '12'
                    },
                    {
                        'candidatura': 'Alcaldía',
                        'candidato_id': '2',
                        'candidato_name': 'Jaime Beltran',
                        'registro_id': '13'
                    },
                    {
                        'candidatura': 'Gobernación',
                        'candidato_id': '3',
                        'candidato_name': 'Juvenal Díaz',
                        'registro_id': '14'
                    },
                    {
                        'candidatura': 'Gobernación',
                        'candidato_id': '3',
                        'candidato_name': 'Hector Mantilla',
                        'registro_id': '14'
                    }
                ]

            },
            {
                'mesa': 3,
                'data': [
                    {
                        'candidatura': 'Alcaldía',
                        'candidato_id': '1',
                        'candidato_name': 'Carlos Sotomonte',
                        'registro_id': '12'
                    },
                    {
                        'candidatura': 'Alcaldía',
                        'candidato_id': '2',
                        'candidato_name': 'Jaime Beltran',
                        'registro_id': '13'
                    },
                    {
                        'candidatura': 'Gobernación',
                        'candidato_id': '3',
                        'candidato_name': 'Juvenal Díaz',
                        'registro_id': '14'
                    },
                    {
                        'candidatura': 'Gobernación',
                        'candidato_id': '3',
                        'candidato_name': 'Hector Mantilla',
                        'registro_id': '14'
                    }
                ]

            },
        ]


        return data

    @staticmethod
    def get_registros_mesas():
        registros = Registro.objects.values(
            'mesa__puesto_votacion__nombre',
            'mesa__numero',
            'testigo__username',
            'testigo__first_name',
        ).distinct().all()

        result = []

        grouped_data = {}
        for item in registros:
            key = (item['mesa__puesto_votacion__nombre'], item['testigo__username'], item['testigo__first_name'])
            if key in grouped_data:
                grouped_data[key]['mesa__numero'].append(item['mesa__numero'])
            else:
                grouped_data[key] = {
                    'mesa__puesto_votacion__nombre': item['mesa__puesto_votacion__nombre'],
                    'testigo__username': item['testigo__username'],
                    'testigo__first_name': item['testigo__first_name'],
                    'mesa__numero': [item['mesa__numero']],
                }

        result = list(grouped_data.values())
        result = sorted(result, key=lambda x: x['mesa__puesto_votacion__nombre'])

        return result


    @staticmethod
    def get_resumen_registros():
        registros = Registro.objects.values(
            'mesa__puesto_votacion__nombre',
            'mesa__numero',
            'testigo__username',
            'testigo__first_name',
            'candidato__nombre',
            'numero_de_votos'
        ).order_by('candidato__id').all()

        result = []

        grouped_data = {}
        for item in registros:
            key = (item['testigo__username'], item['mesa__numero'])
            if key in grouped_data:
                grouped_data[key]['candidatos'].append(item['numero_de_votos'])
            else:
                grouped_data[key] = {
                    'mesa__puesto_votacion__nombre': item['mesa__puesto_votacion__nombre'],
                    'testigo__username': item['testigo__username'],
                    'testigo__first_name': item['testigo__first_name'],
                    'mesa__numero': item['mesa__numero'],
                    'candidatos': [item['numero_de_votos']],
                }

        result = list(grouped_data.values())
        result = sorted(result, key=lambda x: (x['mesa__puesto_votacion__nombre'], x['mesa__numero']))

        return result

    @staticmethod
    def get_resumen_registros_para_graficos():

        registros = Registro.objects.values(
            'candidato__nombre',
            'numero_de_votos'
        ).order_by('candidato__id').all()

        result = Registro.objects.values('candidato__candidatura', 'candidato__nombre') \
            .annotate(total_votos=Sum('numero_de_votos')) \
            .order_by('candidato__id')
        print(result)
        return list(result)
