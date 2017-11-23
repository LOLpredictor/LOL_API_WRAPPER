"""
Create an instance to call the riot API
"""

import requests
import json
import settings
from data import *
from elasticsearch import Elasticsearch
from sources.lib.champion.champion import Champion
from sources.lib.user.user import User
from glob import glob

class API:
    def __init__(self, key):
        self.key = key

    def get_user_data(self,country,name):
        call = requests.get("https://EUW1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"+name)
        content = call.json()
        print(content)
        user = User(country)
        user.user_from_riot_api(content)
        user.to_json()


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
        print("Content : \n" + content)
        champion = Champion.champion_from_riot_api(content)
        return champion


    def get_champions_data(self):
        call = requests.get(
            "https://BR1.api.riotgames.com/lol/static-data/v3/champions?locale=en_US&tags=all&dataById=false&api_key=" + self.key)
        content = call.json()
        champions= []

        for i in range (0 , 517 ):
            try:
                champions.append(content["keys"][str(i)])
            except:
                pass

        print(champions)

        for i in range (0,len(champions)):
            champion = Champion.champion_from_riot_api(content["data"][champions[i]])
            print('../../data/champion/' + champion.name + '.json')
            with open('../../data/champion/' + champion.name + '.json', 'w') as f:
                json.dump(champion.to_dict(), f)


    def send_all_json_champion(self):

        es = Elasticsearch()
        i = 1

        for path in glob('../../data/champion/*.json'):
            print(path)
            print(i)
            with open(path) as data_file:
                data = json.load(data_file)

            es.index(index="champion", doc_type='information_globale', body=data, id=i)
            i += 1

        #champion = Champion.champion_from_riot_api(content)
        #return champion





