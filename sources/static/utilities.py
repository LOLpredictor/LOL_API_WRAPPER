END_URL = '?api_key={}'

# Url to get all the champions of league of legends
URL_BASE_ALL_CHAMPIONS = "https://{}.api.riotgames.com/lol/static-data/v3/champions?locale={}"
END_URL_ALL_CHAMPIONS = "&dataById=false&api_key={}"
URL_ALL_CHAMPIONS = URL_BASE_ALL_CHAMPIONS + "&tags=all" + END_URL_ALL_CHAMPIONS

# Url to get information about a champion in specific
URL_BASE_CHAMPION_ID = "https://{}.api.riotgames.com/lol/static-data/v3/champions/{}?locale={}"
END_URL_CHAMPION_ID = "&api_key={}"
URL_CHAMPION_ID = URL_BASE_CHAMPION_ID + "&tags=all" + END_URL_CHAMPION_ID

# Url to get information about summoner
URL_SUMMONER_BY_NAME = "https://{}.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}" + END_URL
URL_SUMMONER_BY_ACCOUNT = "https://{}.api.riotgames.com/lol/summoner/v3/summoners/by-account/{}" + END_URL

# Language code to get a JSON with the good language
UNITED_KINGDOM = "en_GB"
UNITED_STATE = "en_US"
FRENCH = "fr_FR"
CZECH = "cs_CZ"
GREEK = "el_GR"
POLISH = "pl_PL"
ROMANIAN = "ro_RO"
HUNGARIAN = "hu_HU"
GERMAN = "de_DE"
SPAIN = "es_ES"
ITALIAN = "it_IT"
JAPANESE = "ja_JP"
KOREAN = "ko_KR"
MEXICO = "es_MX"
ARGENTINA = "es_AR"
BREZIL = "pt_BR"
AUSTRALIA = "en_AU"
RUSSIAN = "ru_RU"
TURKISH = "tr_TR"
MALAY = "ms_MY"
PHILIPPINES = "en_PH"
SINGAPORE = "en_SG"
THAI = "th_TH"
VIETNAMESE = "vn_VN"
INDONESIAN = "id_ID"
MALEYSIA = "zh_MY"
CHINA = "zh_CN"
TAIWAN = "zh_TW"

# Country code used to choose the right platform
PLATFORM_EUROPE_NORTH = "eun1"
PLATFORM_EUROPE_WEST = "euw1"
PLATFORM_JAPAN = "jp1"
PLATFORM_KOREAN = "kr"
PLATFORM_BRAZIL = "br1"
PLATFORM_LATIN_AMERICA_NORTH = "la1"
PLATFORM_LATIN_AMERICA_SOUTH = "la2"
PLATFORM_NORTH_AMERICA = "na"
PLATFORM_NORTH_AMERICA_1 = "na1"
PLATFORM_OCEANIA = "oc1"
PLATFORM_RUSSIA = "ru"
PLATFORM_TURKEY = "tr1"
PLATFORM_PUBLIC_BETA_ENVIRONMENT = "pbe1"

# About champion
CHAMPION_INFO = 'info'
CHAMPION_ID = 'id'
CHAMPION_PASSIVE = 'passive'
CHAMPION_STATS = 'stats'
CHAMPION_SKINS = 'skins'
CHAMPION_SPELLS = 'spells'
CHAMPION_TAGS = 'tags'
CHAMPION_LORE = 'lore'
CHAMPION_NAME = 'name'
CHAMPION_PAR_TYPE = 'partype'
CHAMPION_TITLE = 'title'
TAB_CHARACTERISTICS_CHAMPION = [CHAMPION_ID, CHAMPION_INFO, CHAMPION_PASSIVE, CHAMPION_STATS, CHAMPION_SKINS,
                                CHAMPION_SPELLS, CHAMPION_TAGS, CHAMPION_LORE, CHAMPION_NAME, CHAMPION_PAR_TYPE,
                                CHAMPION_TITLE]

# About Summoner
SUMMONER_NAME = 'name'
SUMMONER_ICON_ID = 'profileIconId'
SUMMONER_LEVEL = 'summonerLevel'
SUMMONER_REVISION_DATE = 'revisionDate'
SUMMONER_ID = 'id'
SUMMONER_ACCOUNT_ID = 'accountId'
TAB_CHARACTERISTICS_SUMMONER = [SUMMONER_NAME, SUMMONER_ICON_ID, SUMMONER_LEVEL, SUMMONER_REVISION_DATE,
                                SUMMONER_ID, SUMMONER_ACCOUNT_ID]