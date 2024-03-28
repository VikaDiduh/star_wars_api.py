from star_wars_api import StarWarsApi

api_client = StarWarsApi()

person = api_client.get_person(1)
planet = api_client.get_planet(1)


print(f"Person name:{person.name}")
print(f"Person skin color:{person.skin_color}")
print(f"Person height:{person.height}")
print(f"Person eye_color:{person.eye_color}")
print(f"Person mass :{person.mass}")
print(f"Person birth year:{person.birth_year}")
print(f"Person hair color:{person.hair_color}")

print(f"planet name:{planet.name}")