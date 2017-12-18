from sources.lib.match.ban import Ban

class Team :

    def __init__(self):
        self.firstDragon = None
        self.bans = []
        self.firstInhibitor = None
        self.win = None
        self.firstRiftHerald = None
        self.firstBaron = None
        self.baronKills = -1
        self.riftHeraldKills = -1
        self.firstBlood = -1
        self.teamId = -1
        self.firstTower = None
        self.inhibitorKills = -1
        self.towerKills = -1
        self.dragonKills = -1


    @classmethod
    def data_team_to_object(cls,data):
        obj = cls()
        obj.firstDragon = data["firstDragon"]
        for i in range (len(data["bans"])):
            obj.bans.append(Ban.ban_data_to_object(data["bans"][i]))
        obj.firstInhibitor = data["firstInhibitor"]
        obj.win = data["win"]
        obj.firstRiftHerald = data["firstRiftHerald"]
        obj.firstBaron = data["firstBaron"]
        obj.baronKills = data["baronKills"]
        obj.riftHeraldKills = data["riftHeraldKills"]
        obj.firstBlood = data["firstBlood"]
        obj.teamId = data["teamId"]
        obj.firstTower = data["firstTower"]
        obj.inhibitorKills = data["inhibitorKills"]
        obj.towerKills = data["towerKills"]
        obj.dragonKills = data["dragonKills"]
        return obj


    def to_dict(self):
        bans = []
        for ban in self.bans:
            bans.append(ban.to_dict())
        return dict(
            firstDragon=self.firstDragon,
            firstInhibitor=self.firstInhibitor,
            win=self.win,
            firstRiftHerald=self.firstRiftHerald,
            firstBaron=self.firstBaron,
            baronKills = self.baronKills,
            riftHeraldKills = self.riftHeraldKills,
            firstBlood=self.firstBlood,
            teamId=self.teamId,
            firstTower=self.firstTower,
            inhibitorKills=self.inhibitorKills,
            towerKills=self.towerKills,
            bans = bans,
            dragonKills=self.dragonKills

        )