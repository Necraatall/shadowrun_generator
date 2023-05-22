import random
from enum import Enum


class Relatives(Enum):
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


make_list = list(Relatives)
RELATIVES = random.choice(make_list)
RELATIVES = RELATIVES.value


class Religion(Enum):
    EGYPTIAN = "some_other_value"
    GREEK = "some_other_value"
    KELT = "some_other_value"
    SLOVAN = "some_other_value"


make_list = list(Religion)
RELIGION = random.choice(make_list)
RELIGION = RELIGION.value


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
POSITIVE_CHARACTERISTIC = POSITIVE_CHARACTERISTIC[0].value, POSITIVE_CHARACTERISTIC[1].value


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


# TODO: dopsat popisky - domyslet remeslniky a pod.
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
    CRAFTER = "crafter"             # remeslnik


make_list = list(Social_class)
SOCIAL_CLASS = random.choice(make_list)
SOCIAL_CLASS = SOCIAL_CLASS.value


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


GENDER = random.choice(list(Gender))
GENDER = GENDER.value

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


class Political_lean(Enum):
    APATHETIC = "apathetic"
    FAR_LEFT = "far left"
    LEFT = "left"
    CENTRE = "centre"
    RIGHT = "right"
    FAR_RIGHT = "far right"
    CONSTITUTIONAL_MONARCHY = "constitutional monarchy"
    SERFDOM = "serfdom"
    SLAVERY = "slavery"
    POSPOLITE = "the original pospolite"
    MONARCHY = "monarchy"
    ANARCHY = "anarchy"
    COMUNISM = "comunism"
    AUTOCRACY = "autocracy"
    MAGIOCRACY = "magiocracy"


POLITICAL_LEAN = random.choice(list(Political_lean))
POLITICAL_LEAN = POLITICAL_LEAN.value
