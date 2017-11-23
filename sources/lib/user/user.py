"""
    name : String   # Summoner name
    summonerLevel : String # Summoner level
    id : long  #Summoner ID
    accountID : long #Account ID

"""

import json

class User:
    def __init__(self,country):
        self.name = None
        self.summonerLevel = None
        self.id = None
        self.accountID = None
        self.countryBelong = country


    @classmethod
    def user_from_riot_api(cls, user_data):
        obj = cls()
        obj.name = user_data["name"]
        obj.summonerLevel = user_data["summonerLevel"]
        obj.id = user_data["id"]
        obj.accountID = user_data["accountID"]
        return  obj


    @classmethod
    def to_json(cls):
        obj = cls()
        print('User Created  : ../../data/user/'+obj.countryBelong + "/"+obj.accountID+'.json')
        with open('../../data/user/'+obj.countryBelong + "/"+obj.accountID+'.json', 'w') as f:
            json.dump(obj.to_dict(), f)


    def __str__(self):
        return self.name + " " + str(self.accountID)

    def to_dict(self):
        return dict(
            accountID = self.accountID,
            countryBelong = self.countryBelong,
            id=self.id,
            name = self.name,
            summonerLevel = self.summonerLevel)