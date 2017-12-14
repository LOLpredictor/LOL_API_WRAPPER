from sources.lib.api import API
import settings
import json
import requests

api = API(settings.API_KEY)
#api.get_user_data("EUW1","Jagang")

api.get_match_data("EUW1","2997006172")

#api.get_champions_data()
#api.send_all_json_champion()
