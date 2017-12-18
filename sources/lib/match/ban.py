

class Ban:
    def __init__(self):
        self.championId = -1
        self.pickTurn = -1



    @classmethod
    def ban_data_to_object(cls,data):
        obj = cls()
        obj.championId = data["championId"]
        obj.pickTurn = data["pickTurn"]
        return obj


    def to_dict(self):
        return self.__dict__