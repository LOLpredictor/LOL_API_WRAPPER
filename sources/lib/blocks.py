from sources.lib.items import *

class Blocks:
    def __init__(self):
        self.rec_math = False
        self.items = []
        self.type = ""

    @classmethod
    def blocks_from_champion_endpoint(cls, passive_data):
        obj = cls()
        obj.rec_math = passive_data["recMath"]
        for i in range(0, len(passive_data["items"])):
            obj.items.append(Item.item_from_champion_endpoint(passive_data["items"][i]))
        obj.type = passive_data["type"]
        return obj