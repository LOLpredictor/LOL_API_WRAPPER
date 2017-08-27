from settings import API_KEY
from sources.lib.api import API

api = API(API_KEY)
champion = api.get_champion_data()
print(champion)