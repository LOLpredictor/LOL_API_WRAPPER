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
        call = requests.get("https://acs.leagueoflegends.com" + self.uri + "?api_key=" + settings.API_KEY + "&queue=" + condition)
        try:
            content = call.json()
            data = content["games"]["games"]
            for i in range (len(data)):
                dataMatch = self.getMatch(data[i])
                if(dataMatch != None):
                    game = Game.game_data(dataMatch)
                    print("Création d'un match id : " + str(game.gameID))
                    Game.to_json(game, data[i]["platformId"])
                    self.games.append(game)
        except:
            time.sleep(0.2)
            print("PAUSE")
            pass
    def boucle(self):
        for uri in self.uris:
            CollectionMatch(uri)

    def setPlayers(self):
        for game in self.games:
            for player in game.players:
                self.players.append(player)

    def setUris(self):
        for player in self.players:
            self.uris.append(player.matcHistoryUri)


    def getMatch(self,data):
        insertion = True
        for path in glob('../../data/game/EUW1/*.json'):
            if (path == "../../data/game/EUW1/" + str(data["gameId"]) + ".json"):
                insertion = False
        if (insertion):
            call = requests.get("https://" + str(data["platformId"]) + ".api.riotgames.com/lol/match/v3/matches/" + str(data["gameId"]) + "?api_key=" + settings.API_KEY)
            content = call.json()
        else:
            print("Ce match est déjà dans la BD : " + str(data["gameId"]) )
            content = None

        return content

print(str(len(glob('../../data/game/EUW1/*.json'))))

#cm = CollectionMatch("/v1/stats/player_history/EUW1/22037669")
