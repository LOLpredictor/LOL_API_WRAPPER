""""

    - difficulty_level: integer (Level of difficulty to play this champion [info][difficulty])
    - attack_level: integer (Attack level of the champion [info][attack])
    - defense_level: integer (Defense level of the champion [info][defense])
    - magic_level: integer (Magic level of the champion [info][magic])
"""


class Info:
    def __init__(self):
        self.defense = -1
        self.difficulty = -1
        self.attack = -1
        self.magic = -1

    @classmethod
    def info_from_champion_endpoint(cls, passive_data):
        obj = cls()
        obj.defense = passive_data["defense"]
        obj.difficulty = passive_data["difficulty"]
        obj.attack = passive_data["attack"]
        obj.magic = passive_data["magic"]
        return obj