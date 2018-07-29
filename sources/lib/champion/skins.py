class Skin:

    def __init__(self, id=int, num=int, name=str):
        self.id = id
        self.num = num
        self.name = name

    def __str__(self):
        return 'Skin\'s name : {} - Id : {} - Num : {}'.format(self.name,self.id,self.num)

    def __repr__(self):
        return self.__str__()
"""
import json

class Skin:
    def __init__(self):
        self.num = -1
        self.name = ""
        self.id = -1

    @classmethod
    def skin_from_champion_endpoint(cls, skin_data):
        obj = cls()
        obj.num = skin_data["num"]
        obj.name = skin_data["name"]
        obj.id = skin_data["id"]
        return obj

    def to_dict(self):
        return self.__dict__
"""

