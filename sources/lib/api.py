"""
Create an instance to call the riot API
"""

import requests
from sources.lib.champion import Champion


class API:
    def __init__(self, key):
        self.key = key

    def get_champion_data(self):
        call = requests.get(
            "https://JP1.api.riotgames.com/lol/static-data/v3/champions/34?locale=en_US"
            "&tags=all"
            "&tags=allytips"
            "&tags=blurb"
            "&tags=enemytips"
            "&tags=image"
            "&tags=info"
            "&tags=lore"
            "&tags=partype"
            "&tags=passive"
            "&tags=recommended"
            "&tags=skins"
            "&tags=spells"
            "&tags=stats"
            "&tags=tags"
            "&api_key=" + self.key)
        content = call.json()
        champion = Champion.champion_from_riot_api(content)
        return champion
