"""
Class giving infos on wich type of game this champ can be use
"""

from sources.lib.blocks import *

class Recommended:
    def __init__(self):
        self.mode = ""
        self.champion = ""
        self.type = ""
        self.blocks = []
        self.map = ""
        self.title = ""

    @classmethod
    def recommended_from_champion_endpoint(cls, passive_data):
        obj = cls()
        obj.mode = passive_data["mode"]
        obj.champion = passive_data["champion"]
        obj.type = passive_data["type"]
        for i in range(0, len(passive_data["blocks"])):
            obj.blocks.append(Blocks.blocks_from_champion_endpoint(passive_data["blocks"][i]))
        obj.map = passive_data["map"]
        obj.map = passive_data["title"]
        return obj