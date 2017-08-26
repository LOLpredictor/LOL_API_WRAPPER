"""
This file is the implementation of a champion on league of legends.
The corresponding endpoint is: /lol/static-data/v3/champions/{id}
A Champion has different attribute:
    - champion_id integer (Id of the champion [id])
    - name: string (Name of the champion [name])
    - title: string (Title of the champion [title])
    - image: string (Name of the image of the champion [image][full])
    - tags: list of string (Tags related to the function of the champion [tags])
    - passive: Passive (Passive of the champion [passive])
    - spells: list of Spell (List of spells that the champion can use [spells])
    - ally_tips: list of string (List of tips for the ally of the champion [allytips])
    - enemy_tips: list of string (List of tips for the ennemy of the champion [allytips])
    - lore: String (History of the champion [lore])

    -partype String (What does the spell cost (MANA/RAGE...))
    -stats Stats (return stats of a champion)
    -blurb String (return ?? ... like some description)
    -info Info (return difficulty,attack,defense...)
    -image Image (return info on image of champ)
    -key String (return name ..)??
"""

from sources.lib.spell import *
from sources.lib.passive import *
from sources.lib.stats import *
from sources.lib.info import *
from sources.lib.image import *
from sources.lib.recommended import *
from sources.lib.skins import *


import requests

class Champion:

    # Default constructor, shouldn't be called
    def __init__(self):
        self.champion_id = -1
        self.name = ""
        self.title = ""
        self.tags = []
        self.passive = Passive
        self.spells = []
        self.ally_tips = []
        self.enemy_tips = []
        self.lore = ""
        self.stats = Stats
        self.par_type = ""
        self.blurb = ""
        self.info = Info
        self.image = Image
        self.key = ""
        self.recommended = []
        self.skins = []


    @classmethod
    def champion_constructor(cls,passive_data):
        obj = cls()
        obj.ally_tips =  passive_data["allytips"]
        obj.enemy_tips = passive_data["enemytips"]
        for i in range(0, len(passive_data["spells"])):
            obj.spells.append(Spell.spell_from_champion_endpoint(passive_data["spells"][i], i))
        obj.tags = passive_data["tags"]
        obj.name = passive_data["name"]
        obj.par_type = passive_data["partype"]
        obj.passive = Passive.passive_from_champion_endpoint(passive_data["passive"])
        obj.title = passive_data["title"]
        obj.stats = Stats.stats_from_champion_endpoint(passive_data["stats"])
        obj.blurb = passive_data["blurb"]
        obj.info = Info.info_from_champion_endpoint(passive_data["info"])
        obj.image = Image.image_from_champion_endpoint(passive_data["image"])
        obj.champion_id = passive_data["id"]
        obj.key = passive_data["key"]
        obj.lore = passive_data["lore"]
        for i in range(0, len(passive_data["recommended"])):
            obj.recommended.append(Recommended.recommended_from_champion_endpoint(passive_data["recommended"][i]))
        for i in range(0, len(passive_data["skins"])):
            obj.skins.append(Skin.skin_from_champion_endpoint(passive_data["skins"][i]))
        return obj






call = requests.get(
    "https://EUW1.api.riotgames.com/lol/static-data/v3/champions/34?locale=en_US" \
    "&tags=all" \
    "&tags=allytips&" \
    "tags=blurb" \
    "&tags=enemytips" \
    "&tags=image" \
    "&tags=info" \
    "&tags=lore" \
    "&tags=partype" \
    "&tags=passive" \
    "&tags=recommended" \
    "&tags=skins" \
    "&tags=spells" \
    "&tags=stats" \
    "&tags=tags" \
    "&api_key=")
content = call.json()
print(content)


my_spell = Champion.champion_constructor(content)
print(my_spell.recommended[0].blocks[0].items[0].id)



# todo implement this class (Good luck with that hehe)
# todo check if there is no other important field to get
