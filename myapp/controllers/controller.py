from myapp.models import Registro
from django.db.models import Count

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
            distribucion = list(query.values('id', 'candidato__candidatura', 'candidato__nombre'))

            result_dict = {}

            for item in distribucion:
                candidatura = item.get("candidato__candidatura")
                if candidatura not in result_dict:
                    result_dict[candidatura] = [[str(item.get("id")), item.get("candidato__nombre")]]
                else:
                    result_dict[candidatura].append([str(item.get("id")), item.get("candidato__nombre")])

            return result_dict
        else:
            return {}

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