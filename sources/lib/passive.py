"""
This file is the implementation of a passive on league of legends. A passive has different attributes:
    - description: string (Description of the passive [description])
    - name: string (Name of the passive [name])
    - image: string (Name of the image of the passive [image][full])
"""

import json

class Passive:

    # Default constructor, shouldn't be called
    def __init__(self):
        self.description = ""
        self.name = ""
        self.image = ""

    @classmethod
    def passive_from_champion_endpoint(cls, passive_data):
        obj = cls()
        obj.name = passive_data["name"]
        obj.description = passive_data["description"]
        obj.image = passive_data["image"]["full"]
        return obj

    def to_dict(self):
        return self.__dict__


# todo create a method to_json in the object
# todo create a method save_to_database
# todo create a class method passive_from_database
