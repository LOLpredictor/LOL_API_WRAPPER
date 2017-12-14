
import json

from sources.lib.match.player import Player


class Game:
    def __init__(self):
        self.seasonID = -1
        self.queueId = -1
        self.gameID = -1
        self.players = []


    @classmethod
    def game_data(cls, data):
        obj = cls()
        obj.seasonID = data["seasonId"]
        obj.queueId = data["queueId"]
        obj.gameID = data["gameId"]
        for player in range(0, len(data["participantIdentities"])):  # avoid using meaning less variable like i/j/z in for loop
            obj.players.append(Player.dataPlayerToObject(data["participantIdentities"][player]))
        return obj


    def to_json(self,country):
        print(country)
        print(str(self.gameID))
        print('User Created  : ../../data/game/'+country + "/"+str(self.gameID)[:-1]+'.json')
        with open('../../data/game/'+country + "/"+str(self.gameID)[:-1]+'.json', 'w') as f:
            json.dump(self.to_dict(country), f)


    def to_dict(self,country):
        players_dict = []
        for player in self.players:
            players_dict.append(player.to_dict())
        return dict(
            seasonId = self.seasonID,
            queueId = self.queueId,
            gameId = self.gameID,
            players = players_dict,
            country = country
        )


    def __str__(self):
        return str(self.gameID) + " " + str(self.queueId) + " " + str(self.seasonID)
