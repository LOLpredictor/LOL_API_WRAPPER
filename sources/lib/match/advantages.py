

class Runes :
    def __init__(self):
        self.runeId = -1
        self.rank = -1

    @classmethod
    def data_to_obj(cls, data):
        obj = cls()
        obj.runeId = data["runeId"]
        obj.rank = data["rank"]
        return obj


    def to_dict(self):
        return self.__dict__



class Masteries:
    def __init__(self):
        self.masteryId = -1
        self.rank = -1

    @classmethod
    def data_to_obj(cls, data):
        obj = cls()
        obj.runeId = data["masteryId"]
        obj.rank = data["rank"]
        return obj


    def to_dict(self):
        return self.__dict__