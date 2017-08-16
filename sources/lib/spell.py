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
"""
import requests


class Spell:

    # Default constructor, shouldn't be called
    def __init__(self):
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
    This method build a spell from on of the JSON present in the champion data "spells":
    """
    @classmethod
    def spell_from_champion_endpoint(cls, spell_data):
        obj = cls()
        obj.name = spell_data["name"]
        obj.level_max = spell_data["maxrank"]
        obj.description = spell_data["description"]
        obj.image = spell_data["image"]["full"]
        obj.cost_type = spell_data["costType"]
        obj.range_at_level = spell_data["range"]
        obj.cost_at_level = spell_data["cost"]
        obj.cooldown_at_level = spell_data["cooldown"]
        return obj


# todo create a method to_json in the object
# todo create a method save_to_database
# todo create a class method spell_from_database
# todo There is still some attributes that I didn't take into consideration like the dammage/heal/... from a spell
# todo I need to understand it and think how to serialize it into our object
