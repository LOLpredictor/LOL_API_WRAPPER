
import json

from sources.lib.match.player import Player
from sources.lib.match.team import Team

class Game:
    def __init__(self):
        self.seasonID = -1
        self.queueId = -1
        self.gameID = -1
        self.players = []
        self.teams = []
        self.gameDuration = -1
        self.gameCreation = -1
        self.gameVersion = ""


    @classmethod
    def game_data(cls, data):
        obj = cls()
        obj.seasonID = data["seasonId"]
        obj.queueId = data["queueId"]
        obj.gameID = data["gameId"]
        for teamIndex in range(0, len(data["teams"])):  # avoid using meaning less variable like i/j/z in for loop
            obj.teams.append(Team.data_team_to_object(data["teams"][teamIndex]))
        for playerIndex in range(0, len(data["participantIdentities"])):  # avoid using meaning less variable like i/j/z in for loop
            obj.players.append(Player.dataPlayerToObject(data,playerIndex))

        obj.gameCreation = data["gameCreation"]
        obj.gameDuration = data["gameDuration"]
        obj.gameVersion = data["gameVersion"]

        return obj


    def to_json(self,country):
        print('Game Created  : ../../data/game/'+country + "/"+str(self.gameID)[:-1]+'.json')
        lastNumber = self.gameID % 10
        with open('../../data/game/'+country + "/"+str(self.gameID)[:-1]+ str(lastNumber) + '.json', 'w') as f:
            json.dump(self.to_dict(country), f)


    def to_dict(self,country):
        players_dict = []
        for player in self.players:
            players_dict.append(player.to_dict())
        teams_dict = []
        for team in self.teams:
            teams_dict.append(team.to_dict())
        return dict(
            gameCreation = self.gameCreation,
            gameDuration =self.gameDuration,
            gameVersion = self.gameVersion,
            seasonId = self.seasonID,
            queueId = self.queueId,
            gameId = self.gameID,
            players = players_dict,
            country = country,
            teams = teams_dict
        )


    def __str__(self):
        return str(self.gameID) + " " + str(self.queueId) + " " + str(self.seasonID)
