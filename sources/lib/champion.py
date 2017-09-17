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

    -partype String (What does the spell cost (MANA/RAGE...))
"""

from sources.lib.spell import *
from sources.lib.passive import *
from sources.lib.skins import *
import json


class Champion:
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
        self.defense = -1
        self.difficulty = -1
        self.attack = -1
        self.magic = -1

    @classmethod
    def champion_from_riot_api(cls, champion_data):
        obj = cls()
        obj.ally_tips = champion_data["allytips"]
        obj.enemy_tips = champion_data["enemytips"]
        for i in range(0, len(champion_data["spells"])):
            obj.spells.append(Spell.spell_from_champion_endpoint(champion_data["spells"][i], i))
        obj.tags = champion_data["tags"]
        obj.name = champion_data["name"]
        obj.par_type = champion_data["partype"]
        obj.passive = Passive.passive_from_champion_endpoint(champion_data["passive"])
        obj.title = champion_data["title"]
        obj.blurb = champion_data["blurb"]
        obj.image = champion_data["image"]["full"]
        obj.champion_id = champion_data["id"]
        obj.key = champion_data["key"]
        obj.lore = champion_data["lore"]
        for skin in range(0, len(champion_data["skins"])):  # avoid using meaning less variable like i/j/z in for loop
            obj.skins.append(Skin.skin_from_champion_endpoint(champion_data["skins"][skin]))

        # STATS

        obj.hp_regen = champion_data["stats"]["hpregen"]
        obj.armor_per_level = champion_data["stats"]["armorperlevel"]
        obj.crit = champion_data["stats"]["crit"]
        obj.crit_per_level = champion_data["stats"]["critperlevel"]
        obj.mp = champion_data["stats"]["mp"]
        obj.attack_damage = champion_data["stats"]["attackdamage"]
        obj.hp_regen_per_level = champion_data["stats"]["hpregenperlevel"]
        obj.mp_regen = champion_data["stats"]["mpregen"]
        obj.spell_block_per_level = champion_data["stats"]["spellblockperlevel"]
        obj.attack_range = champion_data["stats"]["attackrange"]
        obj.mp_regen_per_level = champion_data["stats"]["mpregenperlevel"]
        obj.armor = champion_data["stats"]["armor"]
        obj.hp = champion_data["stats"]["hp"]
        obj.attack_damage_per_level = champion_data["stats"]["attackdamageperlevel"]
        obj.mp_per_level = champion_data["stats"]["mpperlevel"]
        obj.attack_speed_per_level = champion_data["stats"]["attackspeedperlevel"]
        obj.hp_per_level = champion_data["stats"]["hpperlevel"]
        obj.spell_block = champion_data["stats"]["spellblock"]
        obj.move_speed = champion_data["stats"]["movespeed"]
        obj.attack_speed_off_set = champion_data["stats"]["attackspeedoffset"]

        #       INFO

        obj.defense = champion_data["info"]["defense"]
        obj.difficulty = champion_data["info"]["difficulty"]
        obj.attack = champion_data["info"]["attack"]
        obj.magic = champion_data["info"]["magic"]
        return obj

    @classmethod
    def get_champion_from_file(cls, file_path="../../data/anivia.json"):
        with open(file_path, 'r') as file:
            champion_data = json.load(file)
        obj = cls.champion_from_riot_api(champion_data)
        return obj

    def __str__(self):
        return self.name + " " + str(self.champion_id)

    def to_dict(self):
        spells_dict = []
        for spell in self.spells:
            spells_dict.append(spell.to_dict())
        skins_dict = []
        for skin in self.skins:
            skins_dict.append(skin.to_dict())
        return dict(
            champion_id=self.champion_id,
            name=self.name,
            title=self.title,
            tags=self.tags,
            passive=self.passive.to_dict(),
            spells=spells_dict,
            ally_tips=self.ally_tips,
            enemy_tips=self.enemy_tips,
            lore=self.lore,
            par_type=self.par_type,
            blurb=self.blurb,
            image=self.image,
            key=self.key,
            recommended=self.recommended,
            skins=skins_dict,
            hp_regen=self.hp_regen,
            armor_per_level=self.armor_per_level,
            crit=self.crit,
            crit_per_level=self.crit_per_level,
            mp=self.mp,
            attack_damage=self.attack_damage,
            hp_regen_per_level=self.hp_regen_per_level,
            mp_regen=self.mp_regen,
            spell_block_per_level=self.spell_block_per_level,
            attack_range=self.attack_range,
            mp_regen_per_level=self.mp_regen_per_level,
            armor=self.armor,
            hp=self.hp,
            attack_damage_per_level=self.attack_damage_per_level,
            mp_per_level=self.mp_per_level,
            attack_speed_per_level=self.attack_speed_per_level,
            hp_per_level=self.hp_per_level,
            spell_block=self.spell_block,
            move_speed=self.move_speed,
            attack_speed_off_set=self.attack_speed_off_set,
            defense=self.defense,
            difficulty=self.difficulty,
            attack=self.attack,
            magic=self.magic,
        )

champion = Champion.get_champion_from_file()
print(champion.to_dict())
