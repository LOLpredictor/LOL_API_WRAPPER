class Skin:
    def __init__(self):
        self.num = -1
        self.name = ""
        self.id = -1

    @classmethod
    def skin_from_champion_endpoint(cls, passive_data):
        obj = cls()
        obj.num = passive_data["num"]
        obj.name = passive_data["name"]
        obj.id = passive_data["id"]
        return obj