"""
This file is the implementation of a passive on league of legends. A passive has different attributes:
    - description: string (Description of the passive [description])
    - name: string (Name of the passive [name])
    - image: string (Name of the image of the passive [image][full])
"""


class Passive:

    # Default constructor, shouldn't be called
    def __init__(self):
        self.description = ""
        self.name = ""
        self.image = ""

    """
    There is no endpoint that provide information about a passive.
    The object is created from the champion endpoint:
        /lol/static-data/v3/champions/{id}
    This method build a passive from the JSON present in the champion data [passive]:
    """
    @classmethod
    def passive_from_champion_endpoint(cls, passive_data):
        obj = cls()
        obj.name = passive_data["name"]
        obj.description = passive_data["description"]
        obj.image = passive_data["image"]["full"]
        return obj


# todo create a method to_json in the object
# todo create a method save_to_database
# todo create a class method passive_from_database
