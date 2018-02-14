"""
Create an instance to call the riot API
"""

import requests
import json
from logging import *
from elasticsearch import Elasticsearch
from sources.lib.champion.champion import Champion
from sources.lib.user.user import User
from glob import glob
from sources.lib.match.game import Game
from sources.lib.match.player import Player
from sources.lib.match.player import Player

class API:
    def __init__(self, key):
        self.nombreRequete = 0
        self.key = key

    def get_user_data(self,country,name):
        call = requests.get("https://"+country+".api.riotgames.com/lol/summoner/v3/summoners/by-name/"+name+"?api_key="+self.key)
        info("Voici l'url d'accès pour l'utilisateur : " + name + " \n https://"+country+".api.riotgames.com/lol/summoner/v3/summoners/by-name/"+name +"?api_key="+self.key)
        content = call.json()
        user = User.user_from_riot_api(content)
        user.to_json(country)

    def get_match_data(self,country,id):
        insertion = True
        for path in glob('../../data/game/EUW1/*.json'):
            if(path == "../../data/game/EUW1/" + str(id) + ".json"):
                print(str(len(glob('../../data/game/EUW1/*.json'))))
                insertion = False

        if(insertion):

            print("Création d'un match.")
            call = requests.get("https://"+country+".api.riotgames.com/lol/match/v3/matches/"+id+"?api_key="+self.key)
            print("Voici l'url d'accès pour accèder au match : " + id + "\n https://"+country+".api.riotgames.com/lol/match/v3/matches/"+id+"?api_key="+self.key)
            content = call.json()
            game = Game.game_data(content)
            Game.to_json(game, country)

            print("Le match : " + id + " à bien été ajouté au fichier. \n")

            try:
                return game.players[0].matcHistoryUri
            except:
                pass
            try:
                return game.players[1].matcHistoryUri
            except:
                log(40,"Error")
        else:
            return None


    def get_match_list(self, uri,condition):
        print("Traitement des matchs de l'uri suivante : " + uri)
        listMatch = []
        lastUri = None
        if(condition == None):
            call = requests.get("https://acs.leagueoflegends.com" + uri + "?api_key=" + self.key )
            print("L'url traitée est la suivante : \n https://acs.leagueoflegends.com" + uri + "?api_key=" + self.key)
        else:
            call = requests.get("https://acs.leagueoflegends.com" + uri + "?api_key=" + self.key + "&queue=" + condition)
            print("L'url traitée est la suivante : https://acs.leagueoflegends.com" + uri + "?api_key=" + self.key + "&queue=" + condition)

        self.nombreRequete += 1
        content =call.json()

        for i in range (len(content["games"]["games"])):
            lastUri = self.get_match_data(content["games"]["games"][i]["platformId"], str(content["games"]["games"][i]["gameId"]))
            self.nombreRequete += 1
            print("Le nombre de requête est de : " + str(self.nombreRequete))
            listMatch.append(content["games"]["games"][i])


        print("L'uri : " + uri + " a bien été traité")

        return listMatch

    def collect_match_data(self,uri,condition):
        newUri = uri
        listUri = [""]
        i = 0
        while(True):
            newUri = self.get_match_list(newUri, condition)
            if(newUri == None):
                newUri = listUri[i]
                print("i : " + str(i) )
                i +=1




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
        for i in range (0,len(champions)):
            champion = Champion.champion_from_riot_api(content["data"][champions[i]])
            print('Le path du Json est le suivant : ../../data/champion/' + champion.name + '.json')
            with open('../../data/champion/' + champion.name + '.json', 'w') as f:
                json.dump(champion.to_dict(), f)

    def send_all_json_game(self):
        es = Elasticsearch()
        for path in glob('../../data/game/EUW1/*.json'):
            print("Le path suivant sera envoyé dans la base elasticsearch : " + path)
            with open(path) as data_file:
                data = json.load(data_file)
            es.index(index="game", doc_type='game_ranked_flex', body=data, id=data["gameId"])


    def send_all_json_champion(self):
        es = Elasticsearch()
        for path in glob('../../data/champion/*.json'):
            print("Le path suivant sera envoyé dans la base elasticsearch : " + path)
            with open(path) as data_file:
                data = json.load(data_file)
            es.index(index="champion", doc_type='information_globale', body=data, id=data["champion_id"])


