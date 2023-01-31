from enum import Enum, auto
import random
from GeneratorJmen.Data.Gods import gods_egypt, gods_greek, gods_kelt, gods_slovan
from GeneratorJmen.generator_jmen import *


#TODO: asi lepe dat zdrojovy kod teto stranky a zkopnout
#    view-source:https://www.character-generator.org.uk/bio/

#TODO: lepsi nez enumy vypadaji listy s random choice
class Gender(Enum):
    MALE = auto()
    FEMALE = auto()

SEXUAL_PREFERENCY_LIST = random.choice(
        "same gender",
        "same gender older",
        "same gender older 10-15 years",
        "same gender older gerontophilia",
        "same gender older 16-25 years",
        "same gender 16-22 year",
        "same gender 30-40 year",
        "same gender 40-50 year",
        "same gender under 16 year",
        "oposite gender",
        "oposite gender older 10-15 years",
        "oposite gender older gerontophilia",
        "oposite gender older 16-25 years",
        "oposite gender 16-22 year",
        "oposite gender 30-40 year",
        "oposite gender 40-50 year",
        "oposite gender under 16 year",
        "bisexual",
        "bisexual older 10-15 years",
        "bisexual older gerontophilia",
        "bisexual older 16-25 years",
        "bisexual 16-22 year",
        "bisexual 30-40 year",
        "bisexual 40-50 year",
        "bisexual under 16 year",
        "group sex",
        "group sex 2 females one male",
        "group sex 2 females one male all others older 10-15 years",
        "group sex 2 females one male all others older gerontophilia",
        "group sex 2 females one male all others older 16-25 years",
        "group sex 2 females one male all others 16-22 year",
        "group sex 2 females one male all others 30-40 year",
        "group sex 2 females one male all others 40-50 year",
        "group sex 2 females one male all others under 16 year",
        "group sex 2 males one female",
        "group sex 2 males one female all others older 10-15 years",
        "group sex 2 males one female all others older gerontophilia",
        "group sex 2 males one female all others older 16-25 years",
        "group sex 2 males one female all others 16-22 year",
        "group sex 2 males one female all others 30-40 year",
        "group sex 2 males one female all others 40-50 year",
        "group sex 2 males one female all others under 16 year",
        "big group sex",
        "gang bang",
        "a game of rape", 
        "sexual non sado maso games",
        "sado maso light",
        "sado maso hard"
)


class Sexual_preferency(Enum):
    SEXUAL_PREFERENCY = random.choice((
        "same gender",
        "same gender older",
        "same gender older 10-15 years",
        "same gender older gerontophilia",
        "same gender older 16-25 years",
        "same gender 16-22 year",
        "same gender 30-40 year",
        "same gender 40-50 year",
        "same gender under 16 year",
        "oposite gender",
        "oposite gender older 10-15 years",
        "oposite gender older gerontophilia",
        "oposite gender older 16-25 years",
        "oposite gender 16-22 year",
        "oposite gender 30-40 year",
        "oposite gender 40-50 year",
        "oposite gender under 16 year",
        "bisexual",
        "bisexual older 10-15 years",
        "bisexual older gerontophilia",
        "bisexual older 16-25 years",
        "bisexual 16-22 year",
        "bisexual 30-40 year",
        "bisexual 40-50 year",
        "bisexual under 16 year",

    ))

class Tribe_name_origin(Enum):
    PL = 1
    NE = 2
    ES = 3
    FR = 4
    GK = 5
    IT = 6
    US = 7
    CZ = 8

class Tribe_surname_origin(Enum):
    PL = 1
    NE = 2
    ES = 3
    FR = 4
    GK = 5
    IT = 6
    US = 7
    CZ = 8

class Social_class(Enum):
    RUNNER = "runner"               # noqa byvalej runner, nebo popripade i modifikace bodu na rozdeleni
    HERO = "hero"                   # noqa mistni hrdina - mozno vice kontaktu, lepsi vztahy nekde - popripade i modifikace bodu na rozdeleni
    UPPER = "upper"
    MIDDLE = "middle"
    WORKING = "working"
    PRIEST = random.choice((
        "priest",
        "mage",
        "shaman"
    )) + " of their society"        # of their society
    TOTAL_JUNKIE = "total_junkie"   # totalni fetak
    HOMELESS = "homeless"           # klasickej homeless chlast
    NATIVE = "native"               # domorodec typu indian... ne cigan
    

class Positive_characteristic(Enum):
    CREATIVE = "creative"
    BRAVE = "brave"
    SMART = "smart"
    EXCITING = "exciting"
    ENERGETIC = "energetic"
    ENTERTAINING = "entertaining"
    INSPIRING = "inspiring"
    GENTLE = "gentle"
    FRIENDLY = "friendly"
    GENEROUS = "generous"
    CONSIDERATE = "considerate"
    BRIGHT = "bright"
    KIND = "kind"
    GIVING = "giving"
    LOVEABLE = "loveable"
    STABLE = "stable"
    ABUNDANT = "abundant"
    ARTISTIC = "artistic"
    APPRECIATIVE = "appreciative"
    AUTHENTIC = "authentic"
    BLESSED = "blessed"
    BLISSFUL = "blissful"
    BEAUTIFUL = "beautiful"
    CALM = "calm"
    CHEERFUL = "cheerful"
    CONFIDENT = "confident"
    DIVINE = "divine"
    DETERMINED = "determined"
    DYNAMIC = "dynamic"
    DAZZLED = "dazzled"
    EMPATHETIC = "empathetic"
    EXUBERANT = "exuberant"
    ENTHUSIASTIC = "enthusiastic"
    ENLIGHTENED = "enlightened"
    FOCUSED = "focused"
    FORGIVING = "forgiving"
    FREE = "free"
    FEARLESS = "fearless"
    GRATEFUL = "grateful"
    GRACEFUL = "graceful"
    GLORIOUS = "glorious"
    HAPPY = "happy"
    HOPEFUL = "hopeful"
    HARMONIOUS = "harmonious"
    HEALTHY = "healthy"
    IMAGINATIVE = "imaginative"
    INSIGHTFUL = "insightful"
    INVENTIVE = "inventive"
    INSPIRED = "inspired"
    JOYFUL = "joyful"
    JOYOUS = "joyous"
    JUST = "just"
    JUBILANT = "jubilant"
    KIND_HEARTED = "kind hearted"
    KNOWLEDGEABLE = "knowledgeable"
    KALON = "kalon"
    LUCKY = "lucky"
    LOVING = "loving"
    LOYAL = "loyal"
    LOVABLE = "lovable"
    MAGIC = "magic"
    MAGNIFICENT = "magnificent"
    MINDFUL = "mindful"
    MOTIVATED = "motivated"
    NOBLE = "noble"
    NOURISHED = "nourished"
    NON_RESISTANT = "non-resistant"
    NICE = "nice"
    OPTIMISTIC = "optimistic"
    OMNISCIENT = "omniscient"
    ORIGINAL = "original"
    OPEN_HEARTED = "open-hearted"
    PEACEFUL = "peaceful"
    PROSPEROUS = "prosperous"
    PERSEVERENT = "perseverent"
    PLAYFUL = "playful"
    QUICK_THINKER = "quick thinker"
    QUIET = "quiet"
    RELAXED = "relaxed"
    RESPECTFUL = "respectful"
    RELIEVED = "relieved"
    RESILIENT = "resilient"
    SERENE = "serene"
    STRONG = "strong"
    SOULFUL = "soulful"
    THOUGHTFUL = "thoughtful"
    THANKFUL = "thankful"
    TRUSTWORTHY = "trustworthy"
    TRANQUIL = "tranquil"
    UPBEAT = "upbeat"
    USEFUL = "useful"
    UNDERSTANDING = "understanding"
    UNIQUE = "unique"
    VIRTUOUS = "virtuous"
    VICTORIOUS = "victorious"
    VIBRANT = "vibrant"
    VALUABLE = "valuable"
    WEALTHY = "wealthy"
    WARMHEARTED = "warmhearted"
    WISE = "wise"
    WORTHY = "worthy"
    XENIAL = "xenial"
    YOUNG = "young at heart"
    ZEALOUS = "zealous"
    ZANY = "zany"
    HEARTWARMING = "heartwarming"
    WILLING_TO_LEARN = "willing to learn"
    EMPOWERED = "empowered"
    WORLD_BUILDER = "world-builder"
    SWEET = "sweet"
    SELFLESS = "selfless"
    SUPERCHARGED = "supercharged"
    WILLING_UNDERSTOOD = "willing understood"
    LIMITLESS = "limitless"
    COURAGEOUS = "courageous"
    WORTHY_TO_TAKE_UP_SPACE = "worthy to take up space"
    SUFFICIENT = "sufficient"
    RESOURCEFUL = "resourceful"


class Negative_characteristic(Enum):
    DISLOYAL = "disloyal"
    SNEAKY = "sneaky"
    UNTRUSTWORTHY = "untrustworthy"
    COWARDLY = "cowardly"
    UNINTELLIGENT = "unintelligent"
    DULL = "dull"
    BORING = "boring"
    LAZY = "lazy"
    RUDE = "rude"
    UNKIND = "unkind"
    STANDOFFISH = "standoffish"
    UNFRIENDLY = "unfriendly"
    STINGY = "stingy"
    GREEDY = "greedy"
    SELFISH = "selfish"
    VIOLENT = "violent"
    UNSTABLE = "unstable"
    SADISTIC = "sadistic"
    EVIL = "evil"
    ABRASIVE = "abrasive"
    ADDICTIVE = "addictive"
    ANTISOCIAL = "antisocial"
    APATHETIC = "apathetic"
    CALLOUS = "callous"
    CATTY = "catty"
    CHILDISH = "childish"
    COCKY = "cocky"
    COMPULSIVE = "compulsive"
    CONFRONTATIONAL = "confrontational"
    CONTROLLING = "controlling"
    CRUEL = "cruel"
    CYNICAL = "cynical"
    DEFENSIVE = "defensive"
    DEVIOUS = "devious"
    DISHONEST = "dishonest"
    DISORGANIZED = "disorganized"
    DISRESPECTFUL = "disrespectful"
    EVASIVE = "evasive"
    EXTRAVAGANT = "extravagant"
    FANATICAL = "fanatical"
    FLAKY = "flaky"
    FOOLISH = "foolish"
    FORGETFUL = "forgetful"
    FRIVOLOUS = "frivolous"
    FUSSY = "fussy"
    GOSSIPY = "gossipy"
    GRUMPY = "grumpy"
    GULLIBLE = "gullible"
    HAUGHTY = "haughty"
    HOSTILE = "hostile"
    HUMORLESS = "humorless"
    HYPOCRITICAL = "hypocritical" 
    IGNORANT = "ignorant"
    IMPATIENT = "impatient"
    IMPULSIVE = "impulsive"
    INATTENTIVE = "inattentive"
    INDECISIVE = "indecisive"
    INFLEXIBLE = "inflexible"
    INHIBITED = "inhibited"
    INSECURE = "insecure"
    IRRATIONAL = "irrational"
    IRRESPONSIBLE = "irresponsible"
    JEALOUS = "jealous"
    JUDGMENTAL = "judgmental"
    KNOW_IT_ALL = "know-it-all"
    MACHO = "macho"
    MANIPULATIVE = "manipulative"
    MARTYR = "martyr"
    MATERIALISTIC = "materialistic"
    MELODRAMATIC = "melodramatic"
    MISCHIEVOUS = "mischievous"
    MORBID = "morbid"
    NAGGING = "nagging"
    NEEDY = "needy"
    NERVOUS = "nervous"
    NOSY = "nosy"
    OBSESSIVE = "obsessive"
    OVERSENSITIVE = "oversensitive"
    PARANOID = "paranoid"
    PERFECTIONIST = "perfectionist"
    PESSIMISTIC = "pessimistic"
    POSSESSIVE = "possessive"
    PREJUDICED = "prejudiced"
    PRETENTIOUS = "pretentious"
    PUSHY = "pushy"
    REBELLIOUS = "rebellious" 
    RECKLESS = "reckless"
    RESENTFUL = "resentful"
    ROWDY = "rowdy"
    SCATTERBRAINED = "scatterbrained"
    SELF_DESTRUCTIVE = "self-destructive"
    SELF_INDULGENT = "self-indulgent"
    SLEAZY = "sleazy"
    SPOILED = "spoiled"
    STUBBORN = "stubborn"
    SUBSERVIENT = "subservient"
    SUPERSTITIOUS = "superstitious"
    SUSPICIOUS = "suspicious"
    TACTLESS = "tactless"
    TEMPERAMENTAL = "temperamental"
    TIMID = "timid"
    UNCOMMUNICATIVE = "uncommunicative"
    UNCOOPERATIVE = "uncooperative"
    UNCOUTH = "uncouth"
    UNETHICAL = "unethical"
    UNGRATEFUL = "ungrateful"
    VAIN = "vain"
    VERBOSE = "verbose"
    VINDICTIVE = "vindictive"
    VOLATILE = "volatile"
    WEAK_WILLED = "weak-willed"
    WHINY = "whiny"
    WITHDRAWN = "withdrawn"
    WORKAHOLIC = "workaholic"
    WORRYWART = "worrywart"


# na zaklade tohoto je mozne resit ze jej nekdo sikanoval ci si na nej nedovolili
class Height(Enum):
    VERY_TALL_HEIGHT = "very tall"
    TALL_HEIGHT = "tall"
    AVERAGE_HEIGHT = "average height"
    SHORT_HEIGHT = "short"
    VERY_SHORT_HEIGHT ="very short"


class Weight(Enum):
    VERY_OVERWEIGHT_WEIGHT = "very overweight"
    OVERWEIGHT_WEIGHT = "overweight"
    AVERAGE_WEIGHT = "average weight"
    UNDERWEIGHT_WEIGHT = "underweight"
    VERY_UNDERWEIGHT_WEIGHT = "very underweight"
    BIG_WEIGHT = "big"
    HEAVYSET_WEIGHT = "heavyset weight"
    THIN_WEIGHT = "thin weight"

class Body(Enum):
    VERY_WELL_BUILT_BODY = "very well-built"
    WELL_BUILD_BODY = "well-built"
    AVERAGE_BUILD_BODY = "average build"
    FINE_BUILD_BODY = "fine build"
    VERY_FINE_BUILD_BODY = "very fine build"
    SKINNY_BUILD_BODY = "skinny build"
    SLENDER_BUILD_BODY = "slender build"

class Body_shape(Enum):
    BOTTOM_HOURGLASS = "bottom hourglass"
    INVERTED_TRINGLE = "inverted tringle"
    DIAMOND = "diamond"
    ATHLETIC = "athletic"
    ROUND = "round"
    RECTANGLE = "rectangle"
    TRIANGLE = "triangle"
    HOURGLASS = "hourglass"
    PEAR = "pear"
    APPLE = "apple"
    TRAPEZOID = "trapezoid"

class Face_shape(Enum):
    OVAL_FACE_SHAPE = "oval" 
    SQUARE_FACE_SHAPE = "square"
    OBLONG_FACE_SHAPE = "oblong"
    TRIANGULAR_FACE_SHAPE = "triangular"
    ROUND_FACE_SHAPE = "round"
    DIAMOND_FACE_SHAPE = "diamond"
    HEART_FACE_SHAPE = "heart"

class Oval_short_hair_styles(Enum):
    PUSHED_BACK_LONG_OVAL_HAIR_STYLE_SHORT = "pushed back long"
    SIDE_PARTED_SHORT_OVAL_HAIR_STYLE_SHORT = "side parted short"
    UNDERCUT_OVAL_HAIR_STYLE_SHORT = "undercut"
    FRINGE_UP_OVAL_HAIR_STYLE_SHORT = "fringe up"

class Square_short_hair_styles(Enum):
    CREW_AKA_BUZZ_CUT_SQUARE_HAIR_STYLE_SHORT = "crew aka buzz cut"
    UNDERCUT_SQUARE_HAIR_STYLE_SHORT = "undercut"
    FAUX_HAWK_SQUARE_HAIR_STYLE_SHORT = "faux hawk"
    SLICKED_BACK_SIDE_PART_SQUARE_HAIR_STYLE_SHORT = "slicked back side part"

class Oblong_short_hair_styles(Enum):
    SIDE_PARTED_OBLONG_HAIR_STYLE_SHORT = "side parted"
    BUZZ_CUT_OBLONG_HAIR_STYLE_SHORT = "buz cut"
    FRINGE_UP_OBLONG_HAIR_STYLE_SHORT = "fringe up"
    SIDE_FRINGE_OBLONG_HAIR_STYLE_SHORT = "side fringe"

class Triangular_short_hair_styles(Enum):
    FRINGE_UP_TRIANGULAR_HAIR_STYLE_SHORT = "fringe up"
    SIDE_FRINGE_TRIANGULAR_HAIR_STYLE_SHORT = "side fringe"
    SIDE_PARTED_TRIANGULAR_HAIR_STYLE_SHORT = "side parted"

class Round_short_hair_styles(Enum):
    FAUX_HAWK_WITH_SHORTER_SIDES_ROUND_HAIR_STYLE_SHORT = "faux hawk with shorter sides"
    FRINGE_UP_ROUND_HAIR_STYLE_SHORT = "fringe up"
    UNDERCUT_ROUND_HAIR_STYLE_SHORT = "undercut"
    QUIFF_ROUND_HAIR_STYLE_SHORT = "quiff"

class Diamond_short_hair_styles(Enum):
    QUIFF_DIAMOND_HAIR_STYLE_SHORT = "quiff"
    LONG_HAIR_PUSHED_BACK_DIAMOND_HAIR_STYLE_SHORT = "long hair pushed back"
    FAUX_HAWK_DIAMOND_HAIR_STYLE_SHORT = "faux hawk"
    SIDE_FRINGE_DIAMOND_HAIR_STYLE_SHORT = "side fringe"

class Heart_short_hair_styles(Enum):
    LONG_FRINGES_HEART_HAIR_STYLE_SHORT = "long fringes"
    SIDE_PARTED_LONG_HEART_HAIR_STYLE_SHORT = "side parted long"
    PUSHED_BACK_HEART_HAIR_STYLE_SHORT = "pushed back"
    UNDERCUT_HEART_HAIR_STYLE_SHORT = "undercut"


# TODO: LONG HAIR
# class Long_hair_styles(Enum):
#     shag_haircut
#     long_curly_hair
#     long_layered
#     long_hairstyle_with_texture_waves
#     long_straight_hair
#     long_hairstyle_with_side_part
#     long_hair_with_middle_part
#     long_surfer_hair
#     long_dreadlocks
#     man_bun
#     man_bun_with_fade
#     long_hairstyle_with_quiff
#     braids_for_man
#     long_half_up
#     long_viking
#     ponytail
#     ponytail_with_undercut
#     long_slick_back
#     bro_flow
#     long_hair_with_bangs
#     shoulder_length_long_hair
#     long_tight_curls
#     long_hairstyle_with_fringe
#     long_hair_dyed_hair
#     mullet_haircut
#     long_hair_with_fade
#     long_hair_with_undercut
#     long_hairstyles_for_men_with_thick_hair
#     long_hair_with_pompadour
#     long_hair_hard_part




# koukni na nested enums
# from enum import Enum

# class _Inside(Enum):
#     Downstairs = 'downstairs'
#     Upstairs = 'upstairs'

# class Location(Enum):
#     Outside = 'outside'
#     Inside = _Inside 

# print(Location.Inside.value.Downstairs.value)
# downstairs


def Hair_style_short(Face_shape: Enum):
    match Face_shape:
        case Face_shape.oval_face_shape:
            random.choice(Oval_short_hair_styles)
        case Face_shape.oval_face_shape:
            random.choice(Square_short_hair_styles)
        case Face_shape.oval_face_shape:
            random.choice(Oblong_short_hair_styles)
        case Face_shape.oval_face_shape:
            random.choice(Triangular_short_hair_styles)
        case Face_shape.oval_face_shape:
            random.choice(Diamond_short_hair_styles)
        case Face_shape.oval_face_shape:
            random.choice(Heart_short_hair_styles)

# udelat to jako: 
# Face_shape.oblong.short.side_parted

# class Hair_style_short(Enum):

#     match Face_shape:
#         case Face_shape.oval_face_shape:
#             random.choice(

#             )

class Hair_color(Enum):
    AUBURN_HAIR_COLOR = 'auburn'
    BROWN_HAIR_COLOR = 'brown'
    BLACK_HAIR_COLOR = 'black'
    BLONDE_HAIR_COLOR = 'blonde'
    COPPER_HAIR_COLOR = 'copper'
    GINGER_HAIR_COLOR = 'ginger'
    GOLDEN_HAIR_COLOR = 'golden'
    GREY_HAIR_COLOR = 'grey'
    MOUSE_HAIR_COLOR = 'mouse'
    RED_HAIR_COLOR = 'red'
    DARK_BROWN_HAIR_COLOR = 'dark brown'
    WHITE_HAIR_COLOR = 'white'

class Hair_types(Enum):
    VERY_STRAIGHT_HAIR_TYPE = "very straight hair"
    STRAIGHT_BEND_HAIR_TYPE = "straight hair with some bends"
    STRAIGHT_COARSER_HAIR_TYPE = "straight hair with coarser texture"
    STRAIGHT_HAIR_TYPE = "straight hair"
    SOFT_WAVE_HAIR_TYPE = "soft wave"
    WAVY_HAIR_TYPE = "wavy"
    DEEP_WAVE_HAIR_TYPE = "deep wave"
    LOST_CURLS_HAIR_TYPE = "lost curls"
    SOFT_CURL_HAIR_TYPE = "soft curl"
    CURLY_HAIR_TYPE = "curly"
    ULTRA_CURLY_HAIR_TYPE = "ultra curly"
    COILED_HAIR_TYPE = "coiled"
    ZIG_ZAG_HAIR_TYPE = "zig zag"
    TIGHTLY_COILED_HAIR_TYPE = "tightly coiled"

#TODO: TOTO: mozna do jineho souboru
class Nationality(Enum):
    AFGHAN = 'Afghan'
    ABORIGIN = 'Aborigin'
    ARGENTINIAN = 'Argentinian'
    SPANISH = 'Spanish'
    AUSTRALIAN = 'Australian'
    BRITISH = 'British'
    AMERICAN = 'American'
    BELGIAN = 'Belgian'
    BRAZILIAN = 'Brazilian'
    WELSH = 'Welsh'
    PORTUGUESE = 'Portuguese'
    CANADIAN = 'Canadian'
    FRENCH = 'French'
    ENGLISH = 'English'
    SCOTTISH = 'Scottish'
    IRISH = 'Irish'
    CORNISH = 'Cornish'
    COLOMBIAN = 'Colombian'
    DANISH = 'Danish'
    EGYPTIAN = 'Egyptian'
    ETHIOPIAN = 'Ethiopian'
    FINNISH = 'Finnish'
    GERMAN = 'German'
    GREEK = 'Greek'
    ITALIAN = 'Italian'
    JAPANESE = 'Japanese'
    MEXICAN = 'Mexican'
    DUTCH = 'Dutch'
    SWEDISH = 'Swedish'
    THAI = 'Thai'
    POLISH = 'Polish'
    HUNGARIAN = 'Hungarian'
    CZECH = 'Czech'
    SLOVAK = 'Slovak'
    AUSTRIAN = 'Austrian'
    UKRAIN = 'Ukrain'
    SLOVENIAN = 'Slovenian'
    HRVAT = 'Hrvat'
    MONTE = 'Monte Negro'
    RUSIAN = 'Rusian'
    CHINEES = 'Chinees'


class Religion(Enum):
    EGYPTIAN = "some_other_value"
    GREEK = "some_other_value"
    KELT = "some_other_value"
    SLOVAN = "some_other_value"

# fce v class musim dat prvni klicovy parametr, ale pak neni staticmethod
# staticmethod nejsou v classe
# pokud v classe potrebuje self
# def neco(klicovy/ridici, prom...)
#     def __init__(self, text: str, rect: dict) -> None:
        # self.text = text
        # self.rect = rect

# def neco(a: int, b: str, c: Nationality):
#     pass

# neco(1, "jedeto", Nationality.Afghan)


eye_color = ('brown', 'black', 'blue', 'green', 'yellow')
hair_color = ('auburn', 'brown', 'black', 'blonde', 'copper', 'ginger', 'golden', 'grey', 'mouse', 'red', 'dark brown', 'white')
skin_tone = ('almond', 'brown', 'bronze', 'chocolate', 'cocoa', 'dark chocolate', 'fair', 'light', 'olive', 'pale', 'walnut')

rase_choice = ('Europoidic', 'Caucasian', 'Latino/Hispanic', 'African', 'Caribbean', 'Middle_Eastern', 'South_Asian', 'East_Asian', 'Mixed')
sub_race_europoidic_choice = ('Nordic', 'Falian', 'Baltic', 'Mediterran', 'Dinaric', 'Alpine')
sub_race_middle_eastern_choices = ('Hamitic', 'Sudeten', 'Oriental')
sub_race_african_choice = ('Hamitic')

race_details = {
    'Europoidic' : {
        "Nordic" : {
            "Vzrůst" : random.choice(("vysoký", "štíhlý")),
            "Postava" : "atletická (respiratorní), široká ramena, pevné držení těla",
            "Končetiny" : "dlouhé ruce a nohy",
            "Tělesná_výška" : "175",
            "Pigmentace" : "světle " + random.choice(("bílá", "narůžovělá, jemná")) + " pleť",
            "Nos" : "dlouhý, úzký, " + random.choice(("rovný", "zahnutý")),
            "Rty" : "tenké",
            "Vlasy" : "světlé " + random.choice(("jemné", "rovné", "vlnité")) + " barvy "
                + random.choice(("šedá", "myší", "zlatá", "blond", "bílá")),
            "Oči" : "světle " + random.choice(("modré", "zelené", "šedé")),
            "Obličej" : "úzký, vysoký",
            "Brada" : random.choice(("úzká", "hranatá", "ostrá")),
            "Lebka" : "dlouhá (dolichocefalie) – lebeční index 75-75,5, obličejový index nad 90",
            "Čelo" : "Ploché, úzké, dozadu sklopené ",
            "Čelist" : "dobře vyvinutá brada",
            "Oblast" : random.choice((
                "severní Evropa",
                "Skandinávský poloostrov",
                "Pobaltí",
                "část Finska",
                "Estonska",
                "Lotyšska a Litvy",
                "severozápadní Polsko",
                "severní Německo",
                "Velká Británie",
                "Irsko",
                "severní Skotsko",
                "Holandsko",
                "Belgie",
                "severní Francie",
                "severní Rusko",
            ))
        },
        "Falian" : {
            "Vzrůst" : "vysoký",
            "Postava" : "robustní, statná (spíše digestivní)",
            "Pigmentace" : "světle bílá",
            "Nos" : "středně široký",
            "Rty" : "tenké",
            "Vlasy" : "světlé",
            "Oči" : "světlé",
            "Obličej" : "široký, poněkud čtvercovitý",
            "Lebka" : "dlouhá (dolichocefalie), lebeční index kolem 75",
            "Čelo" : "strmé, široké, velmi vyvinuté nadočnicové oblouky",
            "Čelist" : "široká a masivní s vystouplou bradou",
            "Oblast" : random.choice((
                "Vestfálsko",
                "střední Švédsko")),
        },
        "Baltic" : {
            "Vzrůst" : random.choice(("malý", "střední")),
            "Postava" : "podsaditá, rovná, široká ramena (digestivní)",
            "Končetiny" : "krátké",
            "Tělesná_výška" : "164",
            "Krk" : "široký, krátký",
            "Pigmentace" : random.choice(("světlá", "žlutošedá")),
            "Nos" : random.choice(("krátký", "mělký")),
            "Vlasy" : random.choice(("pevné", "rovné")) + random.choice(("popelavé", "světlý blond")),
            "Oči" : random.choice(("světle modré", "modrobílé")) + "posazeny daleko od sebe, někdy i polo-mongoloidní tvar",
            "Obličej" : "robustní, široký, vysedlé lícní kosti",
            "Lebka" : "krátká (brachycefalie) – lebeční index 80,9-83,2 ",
            "Čelist" : "masivní s nevystupující bradou",
            "Brada" : random.choice(("kulatá", "ustupující")),
            "Čelo" : "dozadu sklopené",
            "Oblast" : random.choice((
                "východní Evropa" 
                "střední a jižní Polsko",
                "Pobaltí " + random.choice(("Litva", "Lotyšsko", "Estonsko")),
                "Česko",
                "Slovensko",
                "Maďarsko",
                "Ukrajina",
                "Bělorusko",
                "Finsko",
                "Rusko",
                "Skandinávie",
                "Holandsko",
            ))
        },
        "Mediterran" : {
            "Vzrůst" : "nízký",
            "Postava" : "štíhlá (respiratorní), držení pružné",
            "Končetiny" : "v poměru k tělu dlouhé",
            "Tělesná_výška" : "161",
            "Pigmentace" : "hnědobílá",
            "Nos" : random.choice(("rovný", "vysoký", "úzký")) + "s vysokým hřbetem",
            "Rty" : "trochu výraznější oproti nordickému typu",
            "Vlasy" : "tmavé",
            "Čelo" : random.choice(("více strmé a klenuté", "úzké")),
            "Oči" : "tmavě hnědé",
            "Obličej" : "oválný",
            "Brada" : "úzká",
            "Lebka" : "dlouhá (dolichocefalie) – lebeční index 70-75, obličejový index nad 90",
            "Oblast" : random.choice((
                "jižní a západní Evropa",
                "Středomoří",
                "Pádská nížina",
                "pobřeží Černého moře",
                "Španělsko",
                "Portugalsko", 
                "Řecko",
                "část Walesu",
                "jihozápadní Německo",
                "jižní Polsko",
                "částečně jižní a centrální Rusko a Balkán",
            ))
        },
        "Dinaric" : {
            "Vzrůst" : "vysoký",
            "Postava" : "štíhlá, astenická (respiratorní) s nenuceným držením těla",
            "Končetiny" : "dlouhé nohy, kratší ruce",
            "Tělesná_výška" : "174",
            "Krk" : "dlouhý",
            "Pigmentace" : random.choice(("hnědobílá", "tmavší")),
            "Nos" : random.choice(("velký", "úzký", "vysoký", "orlí (konvexní)")),
            "Vlasy" : "silné " + random.choice(("tmavohnědé", "černé")),
            "Oči" : random.choice(("tmavohnědé", "černé")),
            "Uši" : "velké",
            "Obličej" : "úzký, vystouplé lícní kosti",
            "Čelo" : "trochu dozadu sklopené",
            "Lebka" : "krátká (brachycefalie) se zploštělým, ale zakulaceným týlem – lebeční index 85-87, obličejový index 90-93",
            "Čelo" : "relativně vysoké, šikmé, rozvinuté nadočnicové oblouky",
            "Čelist" : "nevýrazná brada",
            "Brada" : random.choice(("široká", "kulatá", "vysoká")),
            "Oblast" : random.choice((
                "jihovýchodní Evropa",
                "Balkánský poloostrov",
                "Chorvatsko",
                "Srbsko",
                "Černá Hora",
                "Bosna a Hercegovina",
                "Albánie",
                "Slovinsko",
                "Bulharsko",
                "Makedonie",
                "Karpaty",
                "Rumunsko",
                "Slovensko",
                "západní Ukrajina",
                "severozápadní Itálie",
                "východní a západní Alpy",
                "Švýcarsko",
                "střední Francie",
                "Pyreneje",
                "Polsko",
                "jižní Německo",
            ))
        },
        "Alpine" : {
            "Vzrůst" : "malý",
            "Tělesná_výška" : "163",
            "Postava" : "podsaditá (digestivní), těžkopádné",
            "Končetiny" : "krátké",
            "Pigmentace" : random.choice(("žlutohnědá", "o něco tlustší")),
            "Nos" : random.choice(("krátký" "tupý")),
            "Vlasy" : "tlusté, pevné " + random.choice(("tmavohnědé", "černé")),
            "Oči" : "tmavohnědé",
            "Obličej" : "široký, kulatý",
            "Lebka" : "krátká (brachycefalie) – lebeční index 84-87, obličejový index nad 80",
            "Čelo" : random.choice(("strmé", "klenuté", "kulaté", "široké")),
            "Čelist" : "široká",
            "Brada" : random.choice(("tupá", "zaoblená")),
            "Oblast" : random.choice(( 
                "střední Evropa",
                "západní Evropa",
                "západní Alpy", 
                "střední Francie",
                "Rakousko",
                "Česko",
                "Švýcarsko",
                "střední Itálie",
                "Slovinsko",
                "jižní Německo",
                "jihozápadní Německo",
                "Maďarsko",
                "jižní Polsko",
            ))
        }

    },
    'Middle_Eastern' : {
        'Hamitic' : {
            "Vzrůst" : "střední",
            "Postava" : "podsaditá (digestivní)",
            "Končetiny" : "krátké",
            "Pigmentace" : "snědá - barvy " + random.choice(("mandle", "olivy", "vlašský ořech")),
            "Nos" : "zahnutý, masitý směrem dolů (podobá se číslici 6)",
            "Rty" : "masité, dolní ret je větší než horní",
            "Vlasy" : "tmavě " + random.choice(("hnědé", "černé", "šedé")) + ", kudrnaté, obočí často srostlé",
            "Oči" : "tmavě " + random.choice(("hnědé", "černé", "zelené")) + ", odhalená vrchní oční víčka (nevyvinuté nadočnicové oblouky)",
            "Uši" : "velké",
            "Obličej" : "středně široký, vystouplé lícní kosti",
            "Lebka" : "krátká (brachycefalie) se zploštělým týlem",
            "Čelo" : "nízké, šikmé, kulaté",
            "Čelist" : "nízká, ustupující brada",
            "Oblast" : random.choice((
                "Blízký východ (Malá Asie)",
                "Kavkaz",
                "Arménie",
                "Asýrie",
                "Ázerbájdžán",
                "Gruzie",
                "Libanon a Sýrie",
            ))
        },
        'Sudeten' : {
            "Vzrůst": "malý",
            "Pigmentace": "tmavší - barvy " + random.choice(("mandle", "olivy", "vlašský ořech")),
            "Nos": "široký, plochý",
            "Vlasy": "tmavě " + random.choice(("hnědé", "černé", "šedé")),
            "Oči": "tmavě " + random.choice(("hnědé", "zelené")),
            "Obličej": "středně široký, výrazné lícní kosti",
            "Lebka": "střední (mesocefalie)",
            "Čelist": "nevystupující brada",
            "Oblast": "východní Evropa",
        },
        'Oriental' : {
            "Vzrůst" : "malý až střední",
            "Postava" : "štíhlá (respiratorní)",
            "Pigmentace" : "snědá - barvy " + random.choice(("mandle", "olivy", "vlašský ořech")),
            "Nos" : "úzký, vysoký",
            "Rty" : "plné",
            "Vlasy" : "tmavě " + random.choice(("hnědé", "černé", "šedé")),
            "Oči" : "tmavě " + random.choice(("hnědé", "černé", "zelené")),
            "Obličej" : "vysoký, převážně úzký a rovný",
            "Lebka" : "dlouhá (dolichocefalie)",
            "Oblast" : random.choice((
                "severní Afrika",
                "Blízký východ",
                "Arábie",
                "Libanon",
                "Irák",
                "Sýrie",
                "Turecko",
                "Degestán a Írán",
            ))
    },
    'African' : {
        'Hamitic' : {
            "Vzrůst" : "vysoký",
            "Postava" : "hodně astenická (respiratorní)",
            "Pigmentace" : "světle " + random.choice(("čokoládová", "kakaová", "ořechová")),
            "Nos" : "rovný",
            "Rty" : "masité",
            "Vlasy" : "kudrnatě " + random.choice(("hnědé", "černé", "šedé")),
            "Oči" : "tmavě "+ random.choice(("hnědé", "černé")),
            "Obličej" : "vysoký",
            "Lebka" : "dlouhá (dolichocefalie)",
            "Oblast" : random.choice((
                "severní Afrika",
                "východní Afrika",
                "jižní Afrika",
            ))
        }
    },
    'Caribbean' : {
        "eye_color" : (eye_color[0], eye_color[1],eye_color[3]),
        "hair_color" : (hair_color[1],hair_color[2],hair_color[7]),
        "skin_tone" : (skin_tone[10], skin_tone[4],skin_tone[3],skin_tone[5])
    },
    'Latino/Hispanic' : {
        "eye_color" : (eye_color[0], eye_color[2], eye_color[3]), 
        "hair_color" : (hair_color[1],hair_color[2],hair_color[7]),
        "skin_tone" : (skin_tone[10], skin_tone[4], skin_tone[3],skin_tone[5], skin_tone[10])
    },
    'Caucasian' : {
        "eye_color" : (eye_color[0], eye_color[2], eye_color[3]),
        "hair_color" : hair_color,
        "skin_tone" : (skin_tone[9], skin_tone[9],skin_tone[8],skin_tone[7],skin_tone[2])
    },
    'South_Asian' : {
        "eye_color" : (eye_color[0], eye_color[1]),
        "hair_color" : (hair_color[1],hair_color[2],hair_color[7]),
        "skin_tone" : (skin_tone[10], skin_tone[8],skin_tone[1])
    },
    'East_Asian' : {
        "eye_color" : (eye_color[0], eye_color[1]),
        "hair_color" : (hair_color[10], hair_color[2],hair_color[7], hair_color[11]),
        "skin_tone" : (skin_tone[9], skin_tone[6], skin_tone[7] ,skin_tone[1])
    },
    'Mixed' : {random.choice((
        'Mestic - potomek Evropana a původního amerického indiána',
        'Mulat - potomek bělocha a černocha',
        'Zambaigo - potomek východního asiata a původního Američana/ eskymáka',
        'Zambo - potomek černocha a Původního Američana',
        'Kajot - potomek mestica a mulata',
        )):
        {
        "eye_color" : (eye_color),
        "hair_color" : (hair_color[1],hair_color[2],hair_color[7],hair_color[3],hair_color[9]),
        "skin_tone" : (skin_tone[9], skin_tone[6], skin_tone[7] ,skin_tone[2], skin_tone[2], skin_tone[8], skin_tone[3])
    }}
}
}

# TODO: nejdrive generovat gender, sexualni preference, rasu, z jake lidske rasy je, 
# zemi puvodu, pak jmeno a pak dalsi
# TODO: lidske/metalidske rasy predelat samostatne
# TODO: vymyslet jak generovat a z ceho - ? - sehnat data net ? zivotni udalosti
# TODO: rozmyslet si lepe adresarovou strukturu
# TODO: printovat bude jeden soubor k tomu urcenej - pokud soubory ci print dict
# TODO: dodelat testy a kouknout na "navrhove vzory" k priprave na dalsi verzi
# TODO: najit cestu jak testovat vysledne stringy ?AI?, 
# slo by pres docstrings a pod kontrolory jazyka?
# - proste promyslet zda by u neceho nebylo lepsi mit jine datove typy, ci to nepostavit jinak
# zda uz nemyslet na reseni pres soubory, spoustec, linux/windows verzi a ospath pokud bude potreba
# / nabidnu at si vybere cestu
# kaslat na Os a jet pres pipenv
# ve 3. verzi mit klikacku webu kde se to bude generovat a ukladat do pdf a pod - pandas
# ve 4. zapojit tu webovku s AI co napises jakej obrazek a vygeneruje ti jej
# ve 4. zapojit tu webovku s AI (pokud je) co nahodim texty a ono mi to vygeneruje zivotni udalosti
# MEMO: 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 key for an openapi
# MEMO: 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 key for an openapi


# print((Gender.gender).value)
# print(random.choice(tuple(Tribe_name_origin)).value)
# print(random.choice(tuple(Tribe_surname_origin)).value)



    
# print(race_detail_type, 'eye_color is : ', random.choice(race_details[race_detail_type][]['eye_color']))
# print(race_detail_type, 'hair_color is : ', random.choice(race_details[race_detail_type]['hair_color']))
# print(race_detail_type, 'skin_tone is : ', random.choice(race_details[race_detail_type]['skin_tone']))

# TODO: done races 
# class print and choose
# TODO: zakomponovat randomizer z shadowrunu
# http://www.miyako.pro/files/Games/Shadowrun/books/Shadowrun%204th%20Edition%20-%20Anniversary.pdf
# https://wrathofzombie.files.wordpress.com/2012/09/shadowrun-background-generator.pdf
# TODO: zapracovat radek od print(random.choice(list(Tribe_name_origin)).value)
# do radku if x in gods_egypt.intent_gods_about_eg:
    # print(gods_egypt.intent_gods_about_eg[x])

###################################################
# New way
###################################################
# Die Roll Clothes Hairstyle Affections
#  1    Biker Leahter       Mohawk                  Tattoos
#  2    Blue Jeans          Long and Grungy         Kick Ass Attitude Glasses
#  3    Fancy Suit          Punked Out              Glowing Tattoos
#  4    Ripped Clothing     Crazy Colors            Spiked Gloves and Belt
#  5    Hot Shorts          Bald                    Interesting Piercings
#  6    High Fashion        Dreds                   Stretched Ear Piercings
#  7    Military Garb       Cut and Clean           Nail Polish that changes color
#  8    Average Clothes     Shaggy                  High Heels or Platform boots
#  9    80s Retro           Afro                    Crazy Colored Contacts
#  10   Costume             Long and Straight       Scarification Art


# 2) Ethnic Origins
# 1 Anglo-American
# 2 African
# 3 European
# 4 Japanese/Koren
# 5 Chinese/Southern Asia
# 6 Pacific Islander
# 7 Hispanic-American
# 8 South American
# 9 Black American
# 10 Central European
