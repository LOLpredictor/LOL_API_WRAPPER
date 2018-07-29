"""
This file is the implementation of a summoner on league of legends.
The corresponding endpoints are: /lol/summoner/v3/summoners/by-name/{summonerName}
                                 /lol/summoner/v3/summoners/by-account/{accountId}
Attributes of a summoner :
    - profileIconId : ID of the summoner icon associated with the summoner
    - name : Summoner name
    - summonerLevel : Summoner level associated with the summoner
    - revisionDate : Date summoner was last modified specified as epoch milliseconds.
     The following events will update this timestamp: profile icon change,
      playing the tutorial or advanced tutorial, finishing a game, summoner name change
    - ID : Summoner ID
    - accountId : Account ID
"""

import json
from utilities import Utility


class User:
    def __init__(self):

        self.name = str()
        self.summonerLevel = str()

        self.id = int()
        self.accountId = int()
        self.profileIconId = int()
        self.revisionDate = None

    @classmethod
    def user_from_riot_api(cls,user_data):
        obj = cls()
        for key in Utility.TAB_CHARACTERISTICS_SUMMONER:
            if key == Utility.SUMMONER_REVISION_DATE:
                object.__setattr__(obj, key, Utility.epoch_to_date_time(user_data[key]))
            else:
                object.__setattr__(obj, key, user_data[key])
        return obj

    def to_json(self,country):
        with open('data/user/{}/{}.json'.format(country,self.accountId), 'w+') as f:
            json.dump(self.to_dict(country), f)

    def __str__(self):
        return self.name + " " + str(self.accountId)

    def to_dict(self,country):
        return dict(
            accountId=self.accountId,
            id=self.id,
            name=self.name,
            summonerLevel=self.summonerLevel,
            profileIconId=self.profileIconId,
            revisionDate=self.revisionDate,
            country=country)