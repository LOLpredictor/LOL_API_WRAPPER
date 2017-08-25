"""
This file is the implementation of a champion on league of legends.
The corresponding endpoint is: /lol/static-data/v3/champions/{id}
A Champion has different attribute:
    - champion_id integer (Id of the champion [id])
    ....
    - difficulty_level: integer (Level of difficulty to play this champion [info][difficulty])
    - attack_level: integer (Attack level of the champion [info][attack])
    - defense_level: integer (Defense level of the champion [info][defense])
    - magic_level: integer (Magic level of the champion [info][magic])
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
    - name: string (Name of the champion [name])
    - title: string (Title of the champion [title])
    - image: string (Name of the image of the champion [image][full])
    - tags: list of string (Tags related to the function of the champion [tags])
    - passive: Passive (Passive of the champion [passive])
    - spells: list of Spell (List of spells that the champion can use [spells])
    - ally_tips: list of string (List of tips for the ally of the champion [allytips])
    - enemy_tips: list of string (List of tips for the ennemy of the champion [allytips])
    - lore: String (History of the champion [lore])
"""

# todo implement this class (Good luck with that hehe)
# todo check if there is no other important field to get
