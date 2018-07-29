from utilities import Utility
from ..champion.champion import Champion
from ..api import API
import operator


class ChampionMastery:

    def __init__(self):
        self.championId = int()
        self.playerId = int()
        self.championLevel = int()
        self.championPoints = int()

        self.championName = str()
        self.lastPlayTime = None

    @classmethod
    def champion_mastery_from_riot_api(cls,data):
        obj = cls()
        for key in Utility.TAB_CHARACTERISTICS_CHAMPION_MASTERY:
            print('key {} - value {}'.format(key,data[key]))
            if key == Utility.CHAMPION_MASTERY_LAST_PLAY:
                object.__setattr__(obj, key, Utility.epoch_to_date_time(data[key]))
            else:
                object.__setattr__(obj, key, data[key])
        return obj

    def __str__(self):
        return 'Champion id : {} - Player id {} - Last Play : {} ' \
               '- Champions points : {}'.format(self.championId,self.playerId,
                                                self.lastPlayTime,self.championPoints)

    def get_name_champion(self,localisation,language):
        print(self.championId)
        champ = Champion.initialize_champion_from_riot_json(API().get_champion_data_id(self.championId,
                                                                                       localisation, language, 'tags'))

        self.championName = champ.name.replace(' ', '')

    @staticmethod
    def top_3_champion_mastery(champions_mastery=list()):
        return sorted(champions_mastery, key=operator.itemgetter(
            Utility.CHAMPION_MASTERY_CHAMPION_POINTS), reverse=True)[:3]


