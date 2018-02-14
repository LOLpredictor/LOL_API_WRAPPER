from sources.lib.api import *
from sources.lib.match.game import *
from sources.lib.match.player import *
import settings
import time

#Variable globale


# 440 represent flexible ranked games
condition = "440"

class CollectionMatch:
    def __init__(self,uri):
        self.uri = uri
        self.games = []
        self.players = []
        self.uris = []

        self.setGames()
        self.setPlayers()
        self.setUris()
        self.boucle()

    def setGames(self):
        t0 = time.time()
        call = requests.get("https://acs.leagueoflegends.com" + self.uri + "?api_key=" + settings.API_KEY + "&queue=" + condition)
        t1 = time.time()

        print("Request uri : " + str(t1-t0))


        try:
            content = call.json()
            data = content["games"]["games"]
            for i in range (len(data)):
                dataMatch = self.getMatch(data[i])
                if(dataMatch != None):
                    t0 = time.time()
                    game = Game.game_data(dataMatch)
                    Game.to_json(game, data[i]["platformId"])
                    self.games.append(game)
                    t1 = time.time()
                    print("Game Created: " + str(t1 - t0))
        except:
            print("PAUSE")
            pass
    def boucle(self):
        for uri in self.uris:
            CollectionMatch(uri)

    def setPlayers(self):
        for game in self.games:
            for player in game.players:
                t0 = time.time()
                self.players.append(player)
                t1 = time.time()
                print("Player Created" + str(t1-t0))

    def setUris(self):
        for player in self.players:
            self.uris.append(player.matcHistoryUri)


    def getMatch(self,data):
        t0 = time.time()
        insertion = True
        for path in glob('../../data/game/EUW1/*.json'):
            if (path == "../../data/game/EUW1/" + str(data["gameId"]) + ".json"):
                insertion = False
        t1 = time.time()

        print("After verification prensence of json file : " + str(t1 - t0))

        t0 = time.time()
        if (insertion):
            call = requests.get("https://" + str(data["platformId"]) + ".api.riotgames.com/lol/match/v3/matches/" + str(data["gameId"]) + "?api_key=" + settings.API_KEY)
            content = call.json()
        else:
            print("Ce match est déjà dans la BD : " + str(data["gameId"]) )
            content = None
        t1 = time.time()

        print("Request matche : " + str(t1 - t0))
        return content

print(str(len(glob('../../data/game/EUW1/*.json'))))
"""
t0  =time.time()
try:
    cm = CollectionMatch("/v1/stats/player_history/EUW1/212059322")
except:
    pass

t1 = time.time()
print("final time : " + str(t1-t0) + "8468")"""