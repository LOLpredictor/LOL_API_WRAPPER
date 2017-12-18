from logging import *
from sources.lib.match.statsPlayer import StatsPlayer
from sources.lib.match.advantages import *
from sources.lib.match.deltas import Deltas

class Player:
    def __init__(self):
        self.summonerId = -1
        self.accountId = -1
        self.participantId = -1
        self.matcHistoryUri = ""
        self.summonerName = ""
        self.currentPlatform = ""
        self.statsPlayer = StatsPlayer
        self.teamId = -1
        self.runes = []
        self.masteries = []
        self.lane = ""
        self.championId = -1
        self.highestAchievedSeasonTier = ""
        self.csDiffPerMinDeltas = None
        self.goldPerMinDeltas = None
        self.xpDiffPerMinDeltas = None
        self.creepsPerMinDeltas = None
        self.xpPerMinDeltas = None
        self.damageTakenDiffPerMinDeltas = None
        self.damageTakenPerMinDeltas = None


    @classmethod
    def dataPlayerToObject(cls, data, playerIndex):
        obj = cls()
        dataParticipant = data["participants"]
        dataPlayer = data["participantIdentities"][playerIndex]["player"]


        # Add player id's
        obj.summonerId = dataPlayer["summonerId"]
        obj.accountId = dataPlayer["accountId"]
        obj.participantId = data["participantIdentities"][playerIndex]["participantId"]
        obj.matcHistoryUri = dataPlayer["matchHistoryUri"]
        obj.summonerName = dataPlayer["summonerName"]
        obj.currentPlatform = dataPlayer["currentPlatformId"]


        if(dataParticipant[playerIndex]["participantId"] != (playerIndex +1)):
            log(40,"Problem participant Id")
            for i in range (dataParticipant):
                if(dataParticipant[i]["participantId"] == (playerIndex + 1)):
                    playerIndex = i

        dataTimeLine = dataParticipant[playerIndex]["timeline"]

        obj.championId = dataParticipant[playerIndex]["championId"]
        obj.lane = dataTimeLine["lane"]
        obj.highestAchievedSeasonTier = dataParticipant[playerIndex]["highestAchievedSeasonTier"]

        try:
            obj.csDiffPerMinDeltas = Deltas.data_to_object(dataTimeLine["csDiffPerMinDeltas"]).to_dict()
        except:
            #log(30, " No csDiffPerMinDeltas in this game")
            pass


        try:
            obj.goldPerMinDeltas = Deltas.data_to_object(dataTimeLine["goldPerMinDeltas"]).to_dict()
        except:
            #log(30, " No goldPerMinDeltas in this game")
            pass

        try:
            obj.xpDiffPerMinDeltas = Deltas.data_to_object(dataTimeLine["xpDiffPerMinDeltas"]).to_dict()
        except:
            #log(30, " No xpDiffPerMinDeltas in this game")
            pass

        try:
            obj.creepsPerMinDeltas = Deltas.data_to_object(dataTimeLine["creepsPerMinDeltas"]).to_dict()
        except:
            #log(30, " No creepsPerMinDeltas in this game")
            pass

        try:
            obj.xpPerMinDeltas = Deltas.data_to_object(dataTimeLine["xpPerMinDeltas"]).to_dict()
        except:
            #log(30, " No xpPerMinDeltas in this game")
            pass

        try:
            obj.damageTakenDiffPerMinDeltas = Deltas.data_to_object(dataTimeLine["damageTakenDiffPerMinDeltas"]).to_dict()
        except:
            #log(30, " No damageTakenDiffPerMinDeltas in this game")
            pass

        try:
            obj.damageTakenPerMinDeltas = Deltas.data_to_object(dataTimeLine["damageTakenPerMinDeltas"]).to_dict()
        except:
            #log(30, " No damageTakenPerMinDeltas in this game")
            pass

        # Add Stats from the player game
        obj.statsPlayer = StatsPlayer.dataStatsPlayerToObject(dataParticipant[playerIndex]["stats"])

        try:
            for i in range (len(dataParticipant[playerIndex]["runes"])):
                obj.runes.append(Runes.data_to_obj(dataParticipant[playerIndex]["runes"][i]))
        except:
            #log(30,"Working with perk")
            pass

        try:
            for i in range (len(dataParticipant[playerIndex]["masteries"])):
                obj.masteries.append(Masteries.data_to_obj(dataParticipant[playerIndex]["masteries"][i]))
        except:
            #log(30,"Masteries reworked")
            pass
        return obj

    def to_dict(self):
        statsPlayer = self.statsPlayer.to_dict()


        runes_dict = []
        for rune in self.runes:
            runes_dict.append(rune.to_dict())

        masteries_dict = []
        for masterie in self.masteries:
            masteries_dict.append(masterie.to_dict())
        return dict(
            championId = self.championId,
            lane = self.lane,
            highestAchievedSeasonTier = self.highestAchievedSeasonTier,
            csDiffPerMinDeltas = self.csDiffPerMinDeltas,
            goldPerMinDeltas = self.goldPerMinDeltas,
            xpDiffPerMinDeltas = self.xpDiffPerMinDeltas,
            creepsPerMinDeltas = self.creepsPerMinDeltas,
            xpPerMinDeltas = self.xpPerMinDeltas,
            damageTakenDiffPerMinDeltas = self.damageTakenDiffPerMinDeltas,
            damageTakenPerMinDeltas = self.damageTakenPerMinDeltas,
            summonerId=self.summonerId,
            accountId=self.accountId,
            participantId=self.participantId,
            matcHistoryUri=self.matcHistoryUri,
            summonerName=self.summonerName,
            currentPlatform = self.currentPlatform,
            statsPlayer = statsPlayer,
            runes = runes_dict,
            masteries = masteries_dict,
            teamId = self.teamId
        )

