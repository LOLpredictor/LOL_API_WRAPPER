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

    - armor_per_level: integer (Armor per level for this champion [stats][armorperlevel])
    - attack_damage: float (Attack damage for this champion [stats][attackdamage])
    - mp_per_level: integer (MP per level for this champion [stats][mpperlevel])
    - mp: float (MP for this champion [stats][mp])
    - armor: float (Armor for this champion [stats][armor])
    - hp: float (hp for this champion [stats][hp])
    - hp_regen_per_level: float (HP regeneration per level for this champion [stats][hpregenperlevel])
    - attack_speed_per_level: float (Attack speed per level for this champion [stats][attackspeedperlevel])
    - attack_range: integer (Attack range for this champion [stats][attackrange])
    - move_speed: integer (Move speed for this champion [stats][movespeed])
    - attack_damage_per_level: float (Attack damage per level for this champion [stats][attackdamageperlevel])
    - mp_regen_per_level: float (MP regeneration per level for this champion [stats][mpregenperlevel])
    - crit_per_level: integer (Critical hit per level for this champion [stats][critperlevel])
    - spell_block_per_level: float (Spell block per level for this champion [stats][spellblockperlevel])
    - crit: integer (Critical hit for this champion [stats][crit])
    - mp_regen: integer (MP regeneration for this champion [stats][mpregen])
    - spell_block: integer (Spell block for this champion [stats][spellblock])
    - hp_regen: float (HP regeneration for this champion [stats][hpregen])
    - hp_per_level: integer (HP per level for this champion [stats][hpperlevel])

    - difficulty_level: integer (Level of difficulty to play this champion [info][difficulty])
    - attack_level: integer (Attack level of the champion [info][attack])
    - defense_level: integer (Defense level of the champion [info][defense])
    - magic_level: integer (Magic level of the champion [info][magic])

    //// What Edwyn add

    -partype String (What does the spell cost (MANA/RAGE...))
    -blurb String (return ?? ... like some description)
    -key String (return name ..)??
"""

from sources.lib.spell import *
from sources.lib.passive import *
from sources.lib.skins import *
from sources.lib.properties import *


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
        self.par_type = ""
        self.blurb = ""
        self.image = ""
        self.key = ""
        self.recommended = []
        self.skins = []

        #          STATS
        self.hp_regen = -1.0
        self.armor_per_level = -1.0
        self.crit = -1.0
        self.crit_per_level = -1.0
        self.mp = -1.0
        self.attack_damage = -1.0
        self.hp_regen_per_level = -1.0
        self.mp_regen = -1.0
        self.spell_block_per_level = -1.0
        self.attack_range = -1.0
        self.mp_regen_per_level = -1.0
        self.armor = -1.0
        self.hp = -1.0
        self.attack_damage_per_level = -1.0
        self.mp_per_level = -1.0
        self.attack_speed_per_level = -1.0
        self.hp_per_level = -1.0
        self.spell_block = -1.0
        self.move_speed = -1.0
        self.attack_speed_off_set = -1.0

        # INFO
        self.defense = -1
        self.difficulty = -1
        self.attack = -1
        self.magic = -1



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
        obj.blurb = passive_data["blurb"]
        obj.image = passive_data["image"]["full"]
        obj.champion_id = passive_data["id"]
        obj.key = passive_data["key"]
        obj.lore = passive_data["lore"]
        for i in range(0, len(passive_data["skins"])):
            obj.skins.append(Skin.skin_from_champion_endpoint(passive_data["skins"][i]))

        obj.hp_regen = passive_data["stats"]["hpregen"]
        obj.armor_per_level = passive_data["stats"]["armorperlevel"]
        obj.crit = passive_data["stats"]["crit"]
        obj.crit_per_level = passive_data["stats"]["critperlevel"]
        obj.mp = passive_data["stats"]["mp"]
        obj.attack_damage = passive_data["stats"]["attackdamage"]
        obj.hp_regen_per_level = passive_data["stats"]["hpregenperlevel"]
        obj.mp_regen = passive_data["stats"]["mpregen"]
        obj.spell_block_per_level = passive_data["stats"]["spellblockperlevel"]
        obj.attack_range = passive_data["stats"]["attackrange"]
        obj.mp_regen_per_level = passive_data["stats"]["mpregenperlevel"]
        obj.armor = passive_data["stats"]["armor"]
        obj.hp = passive_data["stats"]["hp"]
        obj.attack_damage_per_level = passive_data["stats"]["attackdamageperlevel"]
        obj.mp_per_level = passive_data["stats"]["mpperlevel"]
        obj.attack_speed_per_level = passive_data["stats"]["attackspeedperlevel"]
        obj.hp_per_level = passive_data["stats"]["hpperlevel"]
        obj.spell_block = passive_data["stats"]["spellblock"]
        obj.move_speed = passive_data["stats"]["movespeed"]
        obj.attack_speed_off_set = passive_data["stats"]["attackspeedoffset"]

        obj.defense = passive_data["info"]["defense"]
        obj.difficulty = passive_data["info"]["difficulty"]
        obj.attack = passive_data["info"]["attack"]
        obj.magic = passive_data["info"]["magic"]
        return obj

    @staticmethod
    def introduction_champion():
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
            "&api_key=" +Properties().api )
        content = call.json()
        champion = Champion.champion_constructor(content)
        print(champion.name + "\n" + champion.title)


Champion.introduction_champion()

# todo implement this class (Good luck with that hehe)
# todo check if there is no other important field to get
