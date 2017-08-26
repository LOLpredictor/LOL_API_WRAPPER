
class Image:
    def __init__(self):
        self.h = -1
        self.sprite = ""
        self.full = ""
        self.w = -1
        self.x = -1
        self.group = ""
        self.y = -1

    @classmethod
    def image_from_champion_endpoint(cls, passive_data):
        obj = cls()
        obj.h = passive_data["h"]
        obj.sprite = passive_data["sprite"]
        obj.full = passive_data["full"]
        obj.w = passive_data["w"]
        obj.x = passive_data["x"]
        obj.group = passive_data["group"]
        obj.y = passive_data["y"]
        return obj