import settings
import sources.static.utilities as Utility
from sources.lib.api import API
from sources.lib.user.user import User

api = API(settings.API_KEY)

user_1 = User.user_from_riot_api(api.get_summoner(name="melvynator",localisation=Utility.PLATFORM_EUROPE_WEST))
print(user_1)

#api.send_all_json_game()
#api.collect_match_data("/v1/stats/player_history/EUW1/223830393","440")
#api.get_user_data("EUW1","Jagang")
#api.get_match_data("EUW1","53396441")

#api.get_champions_data()
#api.send_all_json_champion()
