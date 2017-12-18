
from logging import *

class StatsPlayer:


    def __init__(self):

        #Champion Level
        self.champLevel = -1

        #Win or Loose
        self.win = None

        # Item of the player
        self.item0 = -1
        self.item1 = -1
        self.item2 = -1
        self.item3 = -1
        self.item4 = -1
        self.item5 = -1
        self.item6 = -1

        #Money
        self.goldSpent = -1
        self.goldEarned = -1


        # Healing stuff
        self.totalHeal = -1
        self.totalUnitsHealed = -1

        # score of warding
        self.visionWardsBoughtInGame = -1
        self.visionScore = -1
        self.wardsKilled = -1
        self.sightWardsBoughtInGame = -1
        self.wardsPlaced = -1

        # Dommage Taken
        self.deaths = -1
        self.totalDamageTaken = -1
        self.physicalDamageTaken = -1
        self.damageSelfMitigated = -1
        self.magicalDamageTaken = -1
        self.trueDamageTaken = -1


        # Dommage Dealt
        self.totalDamageDealt = -1
        self.trueDamageDealt = -1
        self.magicDamageDealt = -1
        self.physicalDamageDealt = -1

        self.trueDamageDealtToChampions = -1
        self.totalDamageDealtToChampions = -1
        self.magicDamDealtToChamp = -1
        self.physicDamageDealtToChamp = -1

        self.largestCriticalStrike = -1

        #About kills
        self.firstBloodKill = None
        self.killingSprees = -1
        self.largestMultiKill = -1
        self.largestKillingSpree = -1
        self.firstBloodAssist = None
        self.kills = -1
        self.assists = -1
        self.doubleKills = -1
        self.tripleKills = -1
        self.quadraKills = -1
        self.pentaKills = -1
        self.unrealKills = -1

        #Total time for crowd control
        self.totalTimeCC = -1
        self.timeCCingOthers = -1

        #Longest time spent living
        self.longestTimeSpentLiving = -1

        #About Minions
        self.totalMinionsKilled = -1
        self.neutralMinionsKilled = -1
        self.neutralMinionsKilledEnemyJungle = -1

        #About tower Hinibitor
        self.firstTowerAssist = None
        self.firstTowerKill = None
        self.firstInhibitorKill = None
        self.firstInhibitorAssist = None

        self.inhibitorKills = -1
        self.turretKills = -1
        self.damageDealtToObjectives = -1
        self.damageDealtToTurrets = -1

        # TODO Actually I don't know the meaning of this data (certainly jungle monster killed) need to check
        self.neutralMinionsKilledTeamJungle = -1

        # TODO the next variables are link to the runes but I don't know their utilities
        # It is link to the masteries and rune but I can't find doc
        self.perkPrimaryStyle = None
        self.perkSubStyle = None

        self.perk0 = -1
        self.perk1 = -1
        self.perk2 = -1
        self.perk3 = -1
        self.perk4 = -1
        self.perk5 = -1

        self.perk0Var1 = -1
        self.perk0Var2 = -1
        self.perk0Var3 = -1

        self.perk1Var1 = -1
        self.perk1Var2 = -1
        self.perk1Var3 = -1

        self.perk2Var1 = -1
        self.perk2Var2 = -1
        self.perk2Var3 = -1

        self.perk3Var1 = -1
        self.perk3Var2 = -1
        self.perk3Var3 = -1

        self.perk4Var1 = -1
        self.perk4Var2 = -1
        self.perk4Var3 = -1

        self.perk5Var1 = -1
        self.perk5Var2 = -1
        self.perk5Var3 = -1


        # TODO understand the players Score meaning
        self.combatPlayerScore = -1
        self.objectivePlayerScore = -1
        self.totalPlayerScore = -1
        self.playerScore0 = -1
        self.playerScore1 = -1
        self.playerScore2 = -1
        self.playerScore3 = -1
        self.playerScore4 = -1
        self.playerScore5 = -1
        self.playerScore6 = -1
        self.playerScore7 = -1
        self.playerScore8 = -1
        self.playerScore9 = -1

        # TODO understand total score rank
        self.totalScoreRank = -1


    @classmethod
    def dataStatsPlayerToObject(cls, data):
        obj = cls()
        problem = False
        obj.win = data["win"]

        obj.item0 = data["item0"]
        obj.item1 = data["item1"]
        obj.item2 = data["item2"]
        obj.item3 = data["item3"]
        obj.item4 = data["item4"]
        obj.item5 = data["item5"]
        obj.item6 = data["item6"]

        obj.champLevel = data["champLevel"]

        try:
            obj.goldSpent = data["goldSpent"]
        except:
            pass

        try:
            obj.goldEarned = data["goldEarned"]
        except:
            pass

        try:
            obj.totalHeal = data["totalHeal"]
        except:
            pass

        try:
            obj.totalUnitsHealed = data["totalUnitsHealed"]
        except:
            pass

        try:
            obj.visionWardsBoughtInGame = data["visionWardsBoughtInGame"]
        except:
            pass
        try:
            obj.visionScore = data["visionScore"]
        except:
            pass

        try:
            obj.wardsKilled = data["wardsKilled"]
        except:
            pass

        try:
            obj.sightWardsBoughtInGame = data["sightWardsBoughtInGame"]
        except:
            pass

        try:
            obj.wardsPlaced = data["wardsPlaced"]
        except:
            pass

        try:
            obj.deaths = data["deaths"]
        except:
            pass

        try:
            obj.totalDamageTaken = data["totalDamageTaken"]
        except:
            pass

        try:
            obj.physicalDamageTaken = data["physicalDamageTaken"]
        except:
            pass

        try:
            obj.damageSelfMitigated = data["damageSelfMitigated"]
        except:
            pass

        try:
            obj.magicalDamageTaken = data["magicalDamageTaken"]
        except:
            pass

        try:
            obj.trueDamageTaken = data["trueDamageTaken"]
        except:
            pass

        try:
            obj.totalDamageDealt = data["totalDamageDealt"]
        except:
            pass

        try:
            obj.trueDamageDealt = data["trueDamageDealt"]
        except:
            pass

        try:
            obj.magicDamageDealt = data["magicDamageDealt"]
        except:
            pass

        try:
            obj.physicalDamageDealt = data["physicalDamageDealt"]
        except:
            pass

        try:
            obj.trueDamageDealtToChampions = data["trueDamageDealtToChampions"]
        except:
            pass

        try:
            obj.totalDamageDealtToChampions = data["totalDamageDealtToChampions"]
        except:
            pass

        try:
            obj.magicDamageDealtToChampions = data["magicDamageDealtToChampions"]
        except:
            pass

        try:
            obj.physicalDamageDealtToChampions = data["physicalDamageDealtToChampions"]
        except:
            pass

        try:
            obj.largestCriticalStrike = data["largestCriticalStrike"]
        except:
            pass

        try:
            obj.firstBloodKill = data["firstBloodKill"]
        except:
            pass

        try:
            obj.killingSprees = data["killingSprees"]
        except:
            pass

        try:
            obj.largestMultiKill = data["largestMultiKill"]
        except:
            pass


        try:
            obj.largestKillingSpree = data["largestKillingSpree"]
        except:
            pass

        try:
            obj.firstBloodAssist = data["firstBloodAssist"]
        except:
            pass

        try:
            obj.kills = data["kills"]
        except:
            pass

        try:
            obj.assists = data["assists"]
        except:pass

        try:
            obj.doubleKills = data["doubleKills"]
        except:
            pass

        try:
            obj.tripleKills = data["tripleKills"]
        except:
            pass

        try:
            obj.quadraKills = data["quadraKills"]
        except:
            pass

        try:
            obj.pentaKills = data["pentaKills"]
        except:
            pass

        try:
            obj.unrealKills = data["unrealKills"]
        except:
            pass

        try:
            obj.totalTimeCC = data["totalTimeCrowdControlDealt"]
        except:
            pass

        try:
            obj.timeCCingOthers = data["timeCCingOthers"]
        except:
            pass

        try:
            obj.longestTimeSpentLiving = data["longestTimeSpentLiving"]
        except:
            pass

        try:
            obj.totalMinionsKilled = data["totalMinionsKilled"]
        except:
            pass

        try:
            obj.neutralMinionsKilled = data["neutralMinionsKilled"]
        except:
            pass

        try:
            obj.neutralMinionsKilledEnemyJungle = data["neutralMinionsKilledEnemyJungle"]
        except:
            pass

        try:
            obj.firstTowerAssist = data["firstTowerAssist"]
        except:
            #log(30, "No information about wich player Has kill the firstTowerAssist")
            pass

        try:
            obj.firstTowerKill = data["firstTowerKill"]
        except:
            #log(30, "No information about wich player Has kill the firstTowerKill")
            pass

        try:
            obj.firstInhibitorKill = data["firstInhibitorKill"]
        except:
            #log(30,"No information about wich player Has kill the first Inhibitor")
            pass

        try:
            obj.firstInhibitorAssist = data["firstInhibitorAssist"]
        except:
            #log(30,"No information about wich player Has kill the firstInhibitorAssist")
            pass

        try:
            obj.inhibitorKills = data["inhibitorKills"]
        except:
            #log(30,"No information about wich player Has kill the inhibitorKills")
            pass

        try:
            obj.turretKills = data["turretKills"]
        except:
            #log(30,"No information about wich player Has kill the turretKills")
            pass

        try:
            obj.damageDealtToObjectives = data["damageDealtToObjectives"]
        except:
            #log(30,"No information about wich player Has kill the damageDealtToObjectives")
            pass

        try:
            obj.damageDealtToTurrets = data["damageDealtToTurrets"]
        except:
            #log(30,"No information about wich player Has kill the damageDealtToTurrets")
            pass

        try:
            obj.neutralMinionsKilledTeamJungle = data["neutralMinionsKilledTeamJungle"]
        except:
            #log(30,"No information about wich player Has kill the neutralMinionsKilledTeamJungle")
            pass


        try:
            obj.perkPrimaryStyle = data["perkPrimaryStyle"]
        except:
            problem = True
            pass


        try:
            obj.perkSubStyle = data["perkSubStyle"]
        except:
            problem = True
            pass

        try:
            obj.perk0 = data["perk0"]
            obj.perk1 = data["perk1"]
            obj.perk2 = data["perk2"]
            obj.perk3 = data["perk3"]
            obj.perk4 = data["perk4"]
            obj.perk5 = data["perk5"]

            obj.perk0Var1 = data["perk0Var1"]
            obj.perk0Var2 = data["perk0Var2"]
            obj.perk0Var3 = data["perk0Var3"]

            obj.perk1Var1 = data["perk1Var1"]
            obj.perk1Var2 = data["perk1Var2"]
            obj.perk1Var3 = data["perk1Var3"]

            obj.perk2Var1 = data["perk2Var1"]
            obj.perk2Var2 = data["perk2Var2"]
            obj.perk2Var3 = data["perk2Var3"]

            obj.perk3Var1 = data["perk3Var1"]
            obj.perk3Var2 = data["perk3Var2"]
            obj.perk3Var3 = data["perk3Var3"]

            obj.perk4Var1 = data["perk4Var1"]
            obj.perk4Var2 = data["perk4Var2"]
            obj.perk4Var3 = data["perk4Var3"]

            obj.perk5Var1 = data["perk5Var1"]
            obj.perk5Var2 = data["perk5Var2"]
            obj.perk5Var3 = data["perk5Var3"]
        except:
            problem = True
            pass


        #if(problem):
            #log(30, "Old version")


        try:
            obj.combatPlayerScore = data["combatPlayerScore"]
        except: pass

        try:
            obj.objectivePlayerScore = data["objectivePlayerScore"]
        except: pass

        try:
            obj.totalPlayerScore = data["totalPlayerScore"]
        except: pass

        obj.playerScore0 = data["playerScore0"]
        obj.playerScore1 = data["playerScore1"]
        obj.playerScore2 = data["playerScore2"]
        obj.playerScore3 = data["playerScore3"]
        obj.playerScore4 = data["playerScore4"]
        obj.playerScore5 = data["playerScore5"]
        obj.playerScore6 = data["playerScore6"]
        obj.playerScore7 = data["playerScore7"]
        obj.playerScore8 = data["playerScore8"]
        obj.playerScore9 = data["playerScore9"]

        try:
            obj.totalScoreRank = data["totalScoreRank"]
        except:
            pass
        return obj

    def to_dict(self):
        return self.__dict__