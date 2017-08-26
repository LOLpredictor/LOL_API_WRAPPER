""""
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
"""



class Stats:
    def __init__(self):
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

    @classmethod
    def stats_from_champion_endpoint(cls, passive_data):
        obj = cls()
        obj.hp_regen = passive_data["hpregen"]
        obj.armor_per_level = passive_data["armorperlevel"]
        obj.crit = passive_data["crit"]
        obj.crit_per_level = passive_data["critperlevel"]
        obj.mp = passive_data["mp"]
        obj.attack_damage = passive_data["attackdamage"]
        obj.hp_regen_per_level = passive_data["hpregenperlevel"]
        obj.mp_regen = passive_data["mpregen"]
        obj.spell_block_per_level = passive_data["spellblockperlevel"]
        obj.attack_range = passive_data["attackrange"]
        obj.mp_regen_per_level = passive_data["mpregenperlevel"]
        obj.armor = passive_data["armor"]
        obj.hp = passive_data["hp"]
        obj.attack_damage_per_level = passive_data["attackdamageperlevel"]
        obj.mp_per_level = passive_data["mpperlevel"]
        obj.attack_speed_per_level = passive_data["attackspeedperlevel"]
        obj.hp_per_level = passive_data["hpperlevel"]
        obj.spell_block = passive_data["spellblock"]
        obj.move_speed = passive_data["movespeed"]
        obj.attack_speed_off_set = passive_data["attackspeedoffset"]
        return obj