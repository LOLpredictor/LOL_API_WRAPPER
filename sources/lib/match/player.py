from sources.lib.user import *

class Player:
    def __init__(self):
        self.summonerId = -1
        self.accountId = -1
        self.participantId = -1
        self.matcHistoryUri = ""
        self.summonerName = ""
        self.currentPlatform = ""

    @classmethod
    def dataPlayerToObject(cls, data):
        obj = cls()
        print(data)
        obj.summonerId = data["player"]["summonerId"]
        obj.accountId = data["player"]["accountId"]
        obj.participantId = data["participantId"]
        obj.matcHistoryUri = data["player"]["matchHistoryUri"]
        obj.summonerName = data["player"]["summonerName"]
        obj.currentPlatform = data["player"]["currentPlatformId"]
        return obj

    def to_dict(self):
        return self.__dict__