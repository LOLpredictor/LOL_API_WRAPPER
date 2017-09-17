"""
This file is the implementation of a spell on league of legends. A spell has different attribute:
    - level_max: integer (Maximum level of the spell)
    - description: string (Description of the spell)
    - name: string (Name of the spell)
    - cost_type: string (What does the spell cost (MANA/RAGE...))
    - range_at_level: list of integer (Range of the spell at all different level)
    - cost_at_level: list of integer (Cost of the spell at all different level)
    - cooldown_at_level: list of floats (Cooldown of the spell at all different level)
    - image: string (Name of the image of the spell)
    - spell_letter: string (letter to cast the spell)
"""

import json

class Spell:

    # Default constructor, shouldn't be called
    def __init__(self):
        self.spell_letter = ""
        self.level_max = -1
        self.description = ""
        self.name = ""
        self.cost_type = ""
        self.image = ""
        self.range_at_level = []
        self.cost_at_level = []
        self.cooldown_at_level = []

    """
    There is no endpoint that provide information about spells.
    The object is created from the champion endpoint:
        /lol/static-data/v3/champions/{id}
    This method build a spell from one of the JSON present in the champion data list [spells]:
    """
    @classmethod
    def spell_from_champion_endpoint(cls, spell_data, indice):
        obj = cls()
        if indice == 0:
            obj.spell_letter = "Q"
        elif indice == 1:
            obj.spell_letter = "w"
        elif indice == 2:
            obj.spell_letter = "E"
        elif indice == 3:
            obj.spell_letter = "R"
        obj.name = spell_data["name"]
        obj.level_max = spell_data["maxrank"]
        obj.description = spell_data["description"]
        obj.image = spell_data["image"]["full"]
        obj.cost_type = spell_data["costType"]
        obj.range_at_level = spell_data["range"]
        obj.cost_at_level = spell_data["cost"]
        obj.cooldown_at_level = spell_data["cooldown"]
        return obj

    def to_dict(self):
        return self.__dict__
