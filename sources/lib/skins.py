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

    def skin_to_json(self):
        return json.dumps(self.__dict__)

print(Skin().skin_to_json())

