from sources.lib.api import API
import settings
import json
import requests

api = API(settings.API_KEY)
api.get_user_data("EUW1","faker")

#api.get_champions_data()
#api.send_all_json_champion()

print(requests.get("https://kr.api.riotgames.com/lol/match/v3/matchlists/by-account/737081").json())