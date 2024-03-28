import requests

from enitity.person import Person
from enitity.planet import Planet


class StarWarsApi:
    def __init__(self):
        self.base_url = 'https://swapi.dev'

    def get_entity(self, entity, entity_id):
        url = f'{self.base_url}/api/{entity}/{entity_id}/'
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f'Неможливо отримати дані для сутності {entity} з індентифікатором {entity_id}')

    def get_person(self, person_id):
        person_dict = self.get_entity('people', person_id)
        return Person(person_dict)

    def get_planet(self, planet_id):
        planet_dict = self.get_entity('planets', planet_id)
        return Planet(planet_dict)
