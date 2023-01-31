from enum import Enum, auto
import random

from Data.Gods import gods_egypt, gods_greek, gods_kelt, gods_slovan

from Data.Name import names
from Data.NickName import nicknames
from Data.Surname import surname

# from ..GeneratorJmen.Data.Gods import gods

# from ..GeneratorAppearance.Data import body as body
# from ..GeneratorAppearance.Data import head as head

intent_tribe_god = (
    gods_egypt.intent_gods_eg,
    gods_greek.intent_gods_about_gk,
    gods_kelt.intent_gods_kelt,
    gods_slovan.intent_gods_slovan,
)

intent_tribe_god_about = (
    gods_egypt.intent_gods_about_eg,
    gods_greek.intent_gods_about_gk,
    gods_kelt.intent_gods_about_kelt,
    gods_slovan.intent_gods_about_slovan,
)


class God:
    @staticmethod
    def get_random_tribe_god_with_abouts():
        return get_random_god_with_abouts()


def get_random_god_with_abouts():
    # vyber list uvnitr listu intent_tribe_god - nevybere jmeno, ale hodnoty
    chosen_list = random.choice(intent_tribe_god)
    # vyber index listu pro pozdejsi pouziti
    get_index_of_tribes_god = intent_tribe_god.index(chosen_list)

    # vybere jednoho boha z listu bohu dle indexu ziskaneho vyse
    chosen_god = random.choice(intent_tribe_god[get_index_of_tribes_god])
    # vybere index vybraneho boha
    get_index_of_god = intent_tribe_god[get_index_of_tribes_god].index(chosen_god)

    # rozsekam vystup na jmeno boha a jeho popis kdy si vemu jen popis
    # vemu si hodnotu popisu boha a dam do stringu
    split_output_chosen_god_about = str(intent_tribe_god_about[get_index_of_tribes_god][get_index_of_god])
    # osetrim aby hodnota nemela nechtene zvlastni znaky
    split_output_chosen_god_about = split_output_chosen_god_about[5:][:-2].replace("'", "")
    # odeslu jmeno boha a popis boha
    return chosen_god, split_output_chosen_god_about




#TODO: asi lepe dat zdrojovy kod teto stranky a zkopnout
#    view-source:https://www.character-generator.org.uk/bio/

#TODO: lepsi nez enumy vypadaji listy s random choice
class Gender(Enum):
    MALE = auto()
    FEMALE = auto()

SEXUAL_PREFERENCY_LIST = random.choice((
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
        "a sexual games",
        "a game of rape", 
        "sexual non sado maso games",
        "sado maso light",
        "sado maso hard", 
        "sex with animals", 
        "froteur",
        "material afilation",
        "sex on public areas", 
        "sex on nature",
        "sex on holy places", 
        "non-maried sex", 
        "sex on brothel", 
        "pasionate sex",
        "bizzare sex", 
        "watching people doing sex", 
        "must be watched when doing sex",
        "sex in the watter", 
        "roleplay",
        "be binded",
        "bind someone",
        "mask on eyes",
        "anal sex", 
        "one night sex",
        "using erotic tools",
        "using food",
        "anal copulation on realy rich places with waterpool", 
        "riping anal by female",
        "double penetration",
        "oral sex with many mans",
        "swinging partners",
        "erotic hypnotic",
        "orgies",
        "realy haired body",
        "the desire to consider oneself a corpse and to be loved as a corpse",
        "the thrill of thunder and lightning",
        "the cancellation of the victim being beaten on the feet with a belt, a cane or even a stick",
        "the thrill of being robbed",
        "the pleasure of looking at or touching a particular substance",
        "is triggered if the sufferer sees their partner crying",
        "torture of the testicles, most commonly crushing or squeezing",
        """he creates situations where strangers can see him naked just by chance. 
        For example, he may leave the curtains open and walk around the apartment naked""",
        "the excitement of observing some work activity or skill of another person",
        "the person in question has a desire to deflower as many women as possible",
        "attachment to sick people",
        "sexual affection for gods, spirits and demons",
        "preferences of partners who are blind or partially sighted",
        "burning the brand with a very high temperature from hot metal, burning with a cigarette or candle flame",
        "sexual arousal on the basis of a hot bath or shower",
        "nipple orgasm",
        "sex with pregnant womans",
        "Multiple orgasm",
        "Orgasm in sleep",
        "Orgasm through erotic fantasies",
        """Coregasm is an interesting response of the body to sport and movement. 
        It is not a targeted sexual stimulation, but a pleasant part of movement, 
        where the erogenous zones are stimulated by movement and rubbing against clothes or sports equipment.""",
        "Latex, vinyl and leather",
        "Voyeurismus",
        "Dendrophilia: raped roots and trunks",
        "Hybristophilia: sex with bad guys",
        "Catoptronophilia: without a mirror not a shot",
        """Salirophilia: you can't be attractive!
        You used to be pretty, but that's not true anymore! 
        Saliophilia consists of the actor dishonoring the object of his desire - usually an attractive person. 
        But it is only about looks, not pain. 
        The salirophiliac will rip the lover's stockings, smear her makeup, mess up her hair, 
        cover her body with mud, and so on. 
        That kinda sucks when you're taking care of yourself! 
        Or do you let something like that go unnoticed?
        """,
        "Transvestitism and sexual orientation on same gender",
        "Transvestitism and sexual orientation on oposite gender",
        "shemale",
        """Erotografomanie
        Arousal is achieved by writing letters with erotic content to unknown objects. 
        The Erotografomaniac is then satisfied by the idea of the woman reading the letter""",
        """Skatophilia
        In scatophilia (or erotophilia) arousal is achieved by anonymous phone calls with erotic content. 
        Men who are aroused by calls with erotic content are usually completely sexually normal.
        """,
        """Tushering
        Arousal is achieved by touching the private parts of anonymous female objects. 
        A tusker usually touches, as if by accident, the breast, ass or genital area of a passing woman in a park or on a vehicle.
        """,
        "Homophilia - a sexual deviation in which a person imagines having sex during a mass or other religious ceremony",
        "Candaulism - this deviation consists in the fact that a partner is sexually satisfied by showing his partner naked in public",
        "Kochwarism - is a dangerous sexual deviation that consists in inducing sexual arousal by strangulation.",
        "Narratophilia - arousal is induced by vulgar words and expressions",
        "Ophidiophilia - ophidiophiles are aroused by snakes",
        "Pyrophilia - a deviation in which sexual arousal is induced by fire",
        "Retifism - a subgroup of fetishism where the erotic stimulus is women's shoes",
        "Somnophilia - a somnophile pisses on a sleeping partner. Often over a complete stranger sleeping, for example in campsites or hostels.",
        "Symphorophilia - a sexual deviation characterized by sexual exhibition in traffic accidents",
        "stealing things.",

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

SOCIAL_CLASS = random.choice(list(Social_class))

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

make_list = list(Positive_characteristic)
POSITIVE_CHARACTERISTIC = random.sample(make_list, 2)
POSITIVE_CHARACTERISTIC = (POSITIVE_CHARACTERISTIC[0].value, POSITIVE_CHARACTERISTIC[1].value)


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

make_list = list(Negative_characteristic)
NEGATIVE_CHARACTERISTIC = random.sample(make_list, 2)
NEGATIVE_CHARACTERISTIC = (NEGATIVE_CHARACTERISTIC[0].value, NEGATIVE_CHARACTERISTIC[1].value)

# na zaklade tohoto je mozne resit ze jej nekdo sikanoval ci si na nej nedovolili
class Height(Enum):
    VERY_TALL_HEIGHT = "very tall"
    TALL_HEIGHT = "tall"
    AVERAGE_HEIGHT = "average height"
    SHORT_HEIGHT = "short"
    VERY_SHORT_HEIGHT ="very short"

make_list = list(Height)
HEIGHT = random.sample(make_list, 2)
HEIGHT = (HEIGHT[0].value, HEIGHT[1].value)

class Weight(Enum):
    VERY_OVERWEIGHT_WEIGHT = "very overweight"
    OVERWEIGHT_WEIGHT = "overweight"
    AVERAGE_WEIGHT = "average weight"
    UNDERWEIGHT_WEIGHT = "underweight"
    VERY_UNDERWEIGHT_WEIGHT = "very underweight"
    BIG_WEIGHT = "big"
    HEAVYSET_WEIGHT = "heavyset weight"
    THIN_WEIGHT = "thin weight"

make_list = list(Weight)
WEIGHT = random.sample(make_list, 2)
WEIGHT = (WEIGHT[0].value, WEIGHT[1].value)

class Body(Enum):
    VERY_WELL_BUILT_BODY = "very well-built"
    WELL_BUILD_BODY = "well-built"
    AVERAGE_BUILD_BODY = "average build"
    FINE_BUILD_BODY = "fine build"
    VERY_FINE_BUILD_BODY = "very fine build"
    SKINNY_BUILD_BODY = "skinny build"
    SLENDER_BUILD_BODY = "slender build"

make_list = list(Body)
BODY = random.sample(make_list, 2)
BODY = (BODY[0].value, BODY[1].value)

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

make_list = list(Body_shape)
BODY_SHAPE = random.sample(make_list, 2)
BODY_SHAPE = (BODY_SHAPE[0].value, BODY_SHAPE[1].value)

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

# udelat to jako: 
# Face_shape.oblong.short.side_parted

# class Hair_style_short(Enum):

#     match Face_shape:
#         case Face_shape.oval_face_shape:
#             random.choice(

#             )


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


# make_list = list(Body_shape)
# BODY_SHAPE = random.sample(make_list, 2)
# BODY_SHAPE = (BODY_SHAPE[0].value, BODY_SHAPE[1].value)

print(SEXUAL_PREFERENCY_LIST)
print(SOCIAL_CLASS)
print(POSITIVE_CHARACTERISTIC)
print(HEIGHT)
print(WEIGHT)
print(BODY)
print(BODY_SHAPE)

print()