from enum import Enum, auto
import random
from GeneratorJmen.Data.Gods import gods_egypt, gods_greek, gods_kelt, gods_slovan
from GeneratorJmen.generator_jmen import *


#TODO: asi lepe dat zdrojovy kod teto stranky a zkopnout
#    view-source:https://www.character-generator.org.uk/bio/

#TODO: lepsi nez enumy vypadaji listy s random choice
class Gender(Enum):
    male = auto()
    female = auto()


class Tribe_name_origin(Enum):
    pl = 1
    ne = 2
    es = 3
    fr = 4
    gk = 5
    it = 6
    us = 7
    cz = 8

class Tribe_surname_origin(Enum):
    pl = 1
    ne = 2
    es = 3
    fr = 4
    gk = 5
    it = 6
    us = 7
    cz = 8

class Social_class(Enum):
    runner = "runner"               # noqa byvalej runner, nebo popripade i modifikace bodu na rozdeleni
    hero = "hero"                   # noqa mistni hrdina - mozno vice kontaktu, lepsi vztahy nekde - popripade i modifikace bodu na rozdeleni
    upper = "upper"
    middle = "middle"
    working = "working"
    priest = random.choice((
        "priest",
        "mage",
        "shaman"
    )) + " of their society"        # of their society
    total_junkie = "total_junkie"   # totalni fetak
    homeless = "homeless"           # klasickej homeless chlast
    native = "native"               # domorodec typu indian... ne cigan
    

class Positive_characteristic(Enum):
    creative = "creative"
    brave = "brave"
    smart = "smart"
    exciting = "exciting"
    energetic = "energetic"
    entertaining = "entertaining"
    inspiring = "inspiring"
    gentle = "gentle"
    friendly = "friendly"
    generous = "generous"
    considerate = "considerate"
    bright = "bright"
    kind = "kind"
    giving = "giving"
    loveable = "loveable"
    stable = "stable"
    abundant = "abundant"
    artistic = "artistic"
    appreciative = "appreciative"
    authentic = "authentic"
    blessed = "blessed"
    blissful = "blissful"
    beautiful = "beautiful"
    calm = "calm"
    cheerful = "cheerful"
    confident = "confident"
    divine = "divine"
    determined = "determined"
    dynamic = "dynamic"
    dazzled = "dazzled"
    empathetic = "empathetic"
    exuberant = "exuberant"
    enthusiastic = "enthusiastic"
    enlightened = "enlightened"
    focused = "focused"
    forgiving = "forgiving"
    free = "free"
    fearless = "fearless"
    grateful = "grateful"
    graceful = "graceful"
    glorious = "glorious"
    happy = "happy"
    hopeful = "hopeful"
    harmonious = "harmonious"
    healthy = "healthy"
    imaginative = "imaginative"
    insightful = "insightful"
    inventive = "inventive"
    inspired = "inspired"
    joyful = "joyful"
    joyous = "joyous"
    just = "just"
    jubilant = "jubilant"
    kind_hearted = "kind hearted"
    knowledgeable = "knowledgeable"
    kalon = "kalon"
    lucky = "lucky"
    loving = "loving"
    loyal = "loyal"
    lovable = "lovable"
    magic = "magic"
    magnificent = "magnificent"
    mindful = "mindful"
    motivated = "motivated"
    noble = "noble"
    nourished = "nourished"
    non_resistant = "non-resistant"
    nice = "nice"
    optimistic = "optimistic"
    omniscient = "omniscient"
    original = "original"
    open_hearted = "open-hearted"
    peaceful = "peaceful"
    prosperous = "prosperous"
    perseverent = "perseverent"
    playful = "playful"
    quick_thinker = "quick thinker"
    quiet = "quiet"
    relaxed = "relaxed"
    respectful = "respectful"
    relieved = "relieved"
    resilient = "resilient"
    serene = "serene"
    strong = "strong"
    soulful = "soulful"
    thoughtful = "thoughtful"
    thankful = "thankful"
    trustworthy = "trustworthy"
    tranquil = "tranquil"
    upbeat = "upbeat"
    useful = "useful"
    understanding = "understanding"
    unique = "unique"
    virtuous = "virtuous"
    victorious = "victorious"
    vibrant = "vibrant"
    valuable = "valuable"
    wealthy = "wealthy"
    warmhearted = "warmhearted"
    wise = "wise"
    worthy = "worthy"
    xenial = "xenial"
    young = "young at heart"
    zealous = "zealous"
    zany = "zany"
    heartwarming = "heartwarming"
    willing_to_learn = "willing to learn"
    empowered = "empowered"
    world_builder = "world-builder"
    sweet = "sweet"
    selfless = "selfless"
    supercharged = "supercharged"
    willing_understood = "willing understood"
    limitless = "limitless"
    courageous = "courageous"
    worthy_to_take_up_space = "worthy to take up space"
    sufficient = "sufficient"
    resourceful = "resourceful"


class Negative_characteristic(Enum):
    disloyal = "disloyal"
    sneaky = "sneaky"
    untrustworthy = "untrustworthy"
    cowardly = "cowardly"
    unintelligent = "unintelligent"
    dull = "dull"
    boring = "boring"
    lazy = "lazy"
    rude = "rude"
    unkind = "unkind"
    standoffish = "standoffish"
    unfriendly = "unfriendly"
    stingy = "stingy"
    greedy = "greedy"
    selfish = "selfish"
    violent = "violent"
    unstable = "unstable"
    sadistic = "sadistic"
    evil = "evil"
    abrasive = "abrasive"
    addictive = "addictive"
    antisocial = "antisocial"
    apathetic = "apathetic"
    callous = "callous"
    catty = "catty"
    childish = "childish"
    cocky = "cocky"
    compulsive = "compulsive"
    confrontational = "confrontational"
    controlling = "controlling"
    cruel = "cruel"
    cynical = "cynical"
    defensive = "defensive"
    devious = "devious"
    dishonest = "dishonest"
    disorganized = "disorganized"
    disrespectful = "disrespectful"
    evasive = "evasive"
    extravagant = "extravagant"
    fanatical = "fanatical"
    flaky = "flaky"
    foolish = "foolish"
    forgetful = "forgetful"
    frivolous = "frivolous"
    fussy = "fussy"
    gossipy = "gossipy"
    grumpy = "grumpy"
    gullible = "gullible"
    haughty = "haughty"
    hostile = "hostile"
    humorless = "humorless"
    hypocritical = "hypocritical" 
    ignorant = "ignorant"
    impatient = "impatient"
    impulsive = "impulsive"
    inattentive = "inattentive"
    indecisive = "indecisive"
    inflexible = "inflexible"
    inhibited = "inhibited"
    insecure = "insecure"
    irrational = "irrational"
    irresponsible = "irresponsible"
    jealous = "jealous"
    judgmental = "judgmental"
    know_it_all = "know-it-all"
    macho = "macho"
    manipulative = "manipulative"
    martyr = "martyr"
    materialistic = "materialistic"
    melodramatic = "melodramatic"
    mischievous = "mischievous"
    morbid = "morbid"
    nagging = "nagging"
    needy = "needy"
    nervous = "nervous"
    nosy = "nosy"
    obsessive = "obsessive"
    oversensitive = "oversensitive"
    paranoid = "paranoid"
    perfectionist = "perfectionist"
    pessimistic = "pessimistic"
    possessive = "possessive"
    prejudiced = "prejudiced"
    pretentious = "pretentious"
    pushy = "pushy"
    rebellious = "rebellious" 
    reckless = "reckless"
    resentful = "resentful"
    rowdy = "rowdy"
    scatterbrained = "scatterbrained"
    self_destructive = "self-destructive"
    self_indulgent = "self-indulgent"
    sleazy = "sleazy"
    spoiled = "spoiled"
    stubborn = "stubborn"
    subservient = "subservient"
    superstitious = "superstitious"
    suspicious = "suspicious"
    tactless = "tactless"
    temperamental = "temperamental"
    timid = "timid"
    uncommunicative = "uncommunicative"
    uncooperative = "uncooperative"
    uncouth = "uncouth"
    unethical = "unethical"
    ungrateful = "ungrateful"
    vain = "vain"
    verbose = "verbose"
    vindictive = "vindictive"
    volatile = "volatile"
    weak_willed = "weak-willed"
    whiny = "whiny"
    withdrawn = "withdrawn"
    workaholic = "workaholic"
    worrywart = "worrywart"


# na zaklade tohoto je mozne resit ze jej nekdo sikanoval ci si na nej nedovolili
class Height(Enum):
    Very_tall_height = "very tall"
    Tall_height = "tall"
    Average_height = "average height"
    Short_height = "short"
    Very_short_height ="very short"


class Weight(Enum):
    Very_overweight_weight = "very overweight"
    Overweight_weight = "overweight"
    Average_weight = "average weight"
    Underweight_weight = "underweight"
    Very_underweight_weight = "very underweight"
    Big_weight = "big"
    Heavyset_weight = "heavyset weight"
    Thin_weight = "thin weight"

class Body(Enum):
    Very_well_built_body = "very well-built"
    Well_build_body = "well-built"
    Average_build_body = "average build"
    Fine_build_body = "fine build"
    Very_fine_build_body = "very fine build"
    Skinny_build_body = "skinny build"
    Slender_build_body = "slender build"

class Body_shape(Enum):
    Bottom_hourglass = "bottom hourglass"
    Inverted_tringle = "inverted tringle"
    Diamond = "diamond"
    Athletic = "athletic"
    Round = "round"
    Rectangle = "rectangle"
    Triangle = "triangle"
    Hourglass = "hourglass"
    Pear = "pear"
    Apple = "apple"
    Trapezoid = "trapezoid"

class Face_shape(Enum):
    Oval_face_shape = "oval" 
    Square_face_shape = "square"
    Oblong_face_shape = "oblong"
    Triangular_face_shape = "triangular"
    Round_face_shape = "round"
    Diamond_face_shape = "diamond"
    Heart_face_shape = "heart"

class Oval_short_hair_styles(Enum):
    pushed_back_long_oval_hair_style_short = "pushed back long"
    side_parted_short_oval_hair_style_short = "side parted short"
    undercut_oval_hair_style_short = "undercut"
    fringe_up_oval_hair_style_short = "fringe up"

class Square_short_hair_styles(Enum):
    crew_aka_buzz_cut_square_hair_style_short = "crew aka buzz cut"
    undercut_square_hair_style_short = "undercut"
    faux_hawk_square_hair_style_short = "faux hawk"
    slicked_back_side_part_square_hair_style_short = "slicked back side part"

class Oblong_short_hair_styles(Enum):
    side_parted_oblong_hair_style_short = "side parted"
    buzz_cut_oblong_hair_style_short = "buz cut"
    fringe_up_oblong_hair_style_short = "fringe up"
    side_fringe_oblong_hair_style_short = "side fringe"

class Triangular_short_hair_styles(Enum):
    fringe_up_triangular_hair_style_short = "fringe up"
    side_fringe_triangular_hair_style_short = "side fringe"
    side_parted_triangular_hair_style_short = "side parted"

class Round_short_hair_styles(Enum):
    faux_hawk_with_shorter_sides_round_hair_style_short = "faux hawk with shorter sides"
    fringe_up_round_hair_style_short = "fringe up"
    undercut_round_hair_style_short = "undercut"
    quiff_round_hair_style_short = "quiff"

class Diamond_short_hair_styles(Enum):
    quiff_diamond_hair_style_short = "quiff"
    long_hair_pushed_back_diamond_hair_style_short = "long hair pushed back"
    faux_hawk_diamond_hair_style_short = "faux hawk"
    side_fringe_diamond_hair_style_short = "side fringe"

class Heart_short_hair_styles(Enum):
    long_fringes_heart_hair_style_short = "long fringes"
    side_parted_long_heart_hair_style_short = "side parted long"
    pushed_back_heart_hair_style_short = "pushed back"
    undercut_heart_hair_style_short = "undercut"


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
    auburn_hair_color = 'auburn'
    brown_hair_color = 'brown'
    black_hair_color = 'black'
    blonde_hair_color = 'blonde'
    copper_hair_color = 'copper'
    ginger_hair_color = 'ginger'
    golden_hair_color = 'golden'
    grey_hair_color = 'grey'
    mouse_hair_color = 'mouse'
    red_hair_color = 'red'
    dark_brown_hair_color = 'dark brown'
    white_hair_color = 'white'

class Hair_types(Enum):
    very_straight_hair_type = "very straight hair"
    straight_bend_hair_type = "straight hair with some bends"
    straight_coarser_hair_type = "straight hair with coarser texture"
    straight_hair_type = "straight hair"
    soft_wave_hair_type = "soft wave"
    wavy_hair_type = "wavy"
    deep_wave_hair_type = "deep wave"
    lost_curls_hair_type = "lost curls"
    soft_curl_hair_type = "soft curl"
    curly_hair_type = "curly"
    ultra_curly_hair_type = "ultra curly"
    coiled_hair_type = "coiled"
    zig_zag_hair_type = "zig zag"
    tightly_coiled_hair_type = "tightly coiled"

#TODO: TOTO: mozna do jineho souboru
class Nationality(Enum):
    AFGHAN = 'Afghan'
    ABORIGIN = 'Aborigin'
    ARGENTINIAN = 'Argentinian'
    Spanish = 'Spanish'
    Australian = 'Australian'
    British = 'British'
    American = 'American'
    Belgian = 'Belgian'
    Brazilian = 'Brazilian'
    Welsh = 'Welsh'
    Portuguese = 'Portuguese'
    Canadian = 'Canadian'
    French = 'French'
    English = 'English'
    Scottish = 'Scottish'
    Irish = 'Irish'
    Cornish = 'Cornish'
    Colombian = 'Colombian'
    Danish = 'Danish'
    Egyptian = 'Egyptian'
    Ethiopian = 'Ethiopian'
    Finnish = 'Finnish'
    German = 'German'
    Greek = 'Greek'
    Italian = 'Italian'
    Japanese = 'Japanese'
    Mexican = 'Mexican'
    Dutch = 'Dutch'
    Swedish = 'Swedish'
    Thai = 'Thai'
    Polish = 'Polish'
    Hungarian = 'Hungarian'
    Czech = 'Czech'
    Slovak = 'Slovak'
    Austrian = 'Austrian'
    Ukrain = 'Ukrain'
    Slovenian = 'Slovenian'
    Hrvat = 'Hrvat'
    Monte = 'Monte Negro'
    Rusian = 'Rusian'
    Chinees = 'Chinees'


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


class Gender(Enum):
    gender = random.choice(("male", "female"))

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

# TODO: sexualni orientaci
# TODO: nejdrive generovat gender, sexualni preference, rasu, z jake lidske rasy je, 
# zemi puvodu, pak jmeno a pak dalsi
# TODO: lidske/metalidske rasy predelat samostatne
# TODO: vymyslet jak generovat a z ceho - ? net ? zivotni udalosti
# TODO: rozmyslet si lepe adresarovou strukturu
# TODO: printovat bude jeden soubor k tomu urcenej
# TODO: dodelat testy a "navrhove vzory" k priprave na dalsi verzi
# - proste promyslet zda by u neceho nebylo lepsi mit jine datove typy, 
# zda uz nemyslet na reseni pres soubory, spoustec, linux/windows verzi a ospath pokud bude potreba
# / nabidnu at si vybere cestu

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
