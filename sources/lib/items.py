class Item:
    def __init__(self):
        self.count = -1
        self.id = -1

    @classmethod
    def item_from_champion_endpoint(cls, passive_data):
        obj = cls()
        obj.count = passive_data["count"]
        obj.id = passive_data["id"]
        return obj