"""
Create an instance to call the riot API
"""

import settings,requests
from utilities import Utility


class API:
    EMPTY_TAB = 0

    def __init__(self):
        self.requestNumber = 0
        self.key = settings.API_KEY

    def get_summoner(self,name=None,account_id=None,localisation=None):
        if all([name,localisation]):
            call = requests.get(Utility.URL_SUMMONER_BY_NAME.format(localisation,name,self.key))
        elif all([account_id,localisation]):
            call = requests.get(Utility.URL_SUMMONER_BY_ACCOUNT.format(localisation,account_id,self.key))
        else:
            raise Exception('The name or the account id and the localisation have to be set!')
        return call.json()

    def get_all_champions_mastery(self,summoner_id=None,localisation=None):
        if all([summoner_id,localisation]):
            call = requests.get(Utility.URL_ALL_CHAMPIONS_MASTERY.format(localisation,summoner_id,self.key))
        else:
            raise Exception('The localisation and the summoner id have to be set!')
        return call.json()

    # Json with a specific champion data
    def get_champion_data_id(self, id, localisation, language, *args):
        if len(args) == API.EMPTY_TAB:
            call = requests.get(Utility.URL_CHAMPION_ID.format(localisation,id,language, self.key))
        else:
            call = requests.get(API._prepare_request(Utility.URL_BASE_CHAMPION_ID
                                                     , Utility.END_URL_CHAMPION_ID, args).format(localisation,
                                                                                                 id, language, *args,
                                                                                                 self.key))
        print(API._prepare_request(Utility.URL_BASE_CHAMPION_ID
                                                     , Utility.END_URL_CHAMPION_ID, args).format(localisation,
                                                                                                 id, language, *args,
                                                                                                 self.key))

        print(call.json())
        return call.json()

    #  Add all tags for request
    @staticmethod
    def _prepare_request(url_base, url_end, args):
        for info in [x for x in args if isinstance(x, str)]:
            url_base += "&tags={}"
        url_base += url_end
        return url_base


"""

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
                print(type(data))
            #es.index(index="champion", doc_type='information_globale', body=data, id=data["champion_id"])
"""


