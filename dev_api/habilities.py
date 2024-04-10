# Classe relacionada a dev_api_restful por meio do import.
from flask import request
from flask_restful import Resource, abort

habilities_list = ['Python', 'Java', 'Flask', 'PHP']

class Habilities(Resource):
    def get(self):
        # Retorna a lista de habilidades
        return habilities_list

    def post(self):
        # Adiciona uma nova habilidade à lista
        # para testar o POST no postman ex: "hability": "Docker"
        new_hability = request.json.get('hability')  # Obtém a nova habilidade do corpo da requisição JSON
        if new_hability not in habilities_list:  # Verifica se a habilidade já existe na lista
            habilities_list.append(new_hability)  # Adiciona a nova habilidade à lista
            return {'message': f'Habilidade {new_hability} adicionada com sucesso.'}, 201  # Retorna uma mensagem de sucesso
        else:
            return {'error': f'A habilidade {new_hability} já existe.'}, 400  # Retorna uma mensagem de erro se a habilidade já existir

class HabilitiesModifier(Resource):
    def put(self, id):
        # Atualiza uma habilidade na lista
        if id < len(habilities_list):  # Verifica se a posição especificada existe na lista
            new_hability = request.json.get('hability')  # Obtém a nova habilidade do corpo da requisição JSON
            if new_hability not in habilities_list:  # Verifica se a nova habilidade já existe na lista
                habilities_list[id] = new_hability  # Atualiza a habilidade na posição especificada com a nova habilidade
                return {'message': f'Habilidade na posição {id} atualizada para {new_hability}.'}, 200  # Retorna uma mensagem de sucesso
            else:
                return {'error': f'A habilidade {new_hability} já existe.'}, 400  # Retorna uma mensagem de erro se a nova habilidade já existir
        else:
            return {'error': f'Posição {id} não encontrada na lista de habilidades.'}, 404  # Retorna uma mensagem de erro se a posição especificada não existir na lista

    def delete(self, id):
        # Deleta uma habilidade da lista
        if id < len(habilities_list):  # Verifica se a posição especificada existe na lista
            deleted_hability = habilities_list.pop(id)  # Remove a habilidade na posição especificada da lista
            return {'message': f'Habilidade na posição {id} removida: {deleted_hability}.'}, 200  # Retorna uma mensagem de sucesso
        else:
            return {'error': f'Posição {id} não encontrada na lista de habilidades.'}, 404  # Retorna uma mensagem de erro se a posição especificada não existir na lista
