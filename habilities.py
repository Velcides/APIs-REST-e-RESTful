# Classe relacionada a dev_api_restful por meio do import.
from flask_restful import Resource

habilities_list = ['Python', 'Java', 'Flask', 'PHP']
class Habilities(Resource):
    def get(self):
        return habilities_list