from sources.lib.api import API
from settings import API_KEY

api = API(API_KEY)

print(api.get_champion_data().champion_to_json())

