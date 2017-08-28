from settings import API_KEY
from sources.lib.api import API

api = API(API_KEY)

print(api.champion_to_json())
