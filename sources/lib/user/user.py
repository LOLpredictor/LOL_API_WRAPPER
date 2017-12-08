"""
    name : String   # Summoner name
    summonerLevel : String # Summoner level
    id : long  #Summoner ID
    accountID : long #Account ID

"""

import json

class User:
    def __init__(self):
        self.name = ""
        self.summonerLevel = ""
        self.id = 0
        self.accountID = 0



    @classmethod
    def user_from_riot_api(cls, user_data):
        obj = cls()
        print(user_data)
        obj.name = user_data["name"]
        obj.summonerLevel = user_data["summonerLevel"]
        obj.id = user_data["id"]
        obj.accountID = user_data["accountId"]
        return  obj



    def to_json(self,country):
        print('User Created  : ../../data/user/'+country + "/"+str(self.accountID)[:-1]+'.json')
        with open('../../data/user/'+country + "/"+str(self.accountID)[:-1]+'.json', 'w') as f:
            json.dump(self.to_dict(country), f)


    def __str__(self):
        return self.name + " " + str(self.accountID)

    def to_dict(self,country):
        return dict(
            accountID = self.accountID,
            id=self.id,
            name = self.name,
            summonerLevel = self.summonerLevel,
            country = country)