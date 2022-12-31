from enum import Enum, auto
import random
from GeneratorJmen.Data.Gods import gods_egypt, gods_greek, gods_kelt, gods_slovan


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

#nutno dovymyslet dalsi, aby jsme s nimi i mohli pocitat jinde
class Physical_characteristic(Enum):
    sexy = "sexy"
    handsome = "handsome"
    beautiful = "beautiful"
    tall = "tall"
    short = "short"

class Social_class(Enum):
    runner = "runner"               # noqa byvalej runner, nebo popripade i modifikace bodu na rozdeleni
    hero = "hero"                   # noqa mistni hrdina - mozno vice kontaktu, lepsi vztahy nekde - popripade i modifikace bodu na rozdeleni
    upper = "upper"
    middle = "middle"
    working = "working"
    priest = "priest"               # popripade shaman
    total_junkie = "total_junkie"      #totalni fetak
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

# na zaklade tohoto je mozne resit ze jej nekdo sikanoval ci si na nej nedovolili
class Height(Enum):
    very_tall = "very tall"
    tall = "tall"
    average = "average"
    short = "short"
    very_short ="very short"


class Weight(Enum):
    very_overweight = "very overweight"
    overweight = "overweight"
    average = "average"
    underweight = "underweight"
    very_underweight = "very underweight"


class Build(Enum):
    very_well_built = "very well-built"
    well_built = "well-built"
    average_build = "average build"
    fine_build = "fine build"
    very_fine_build = "very fine build"


class Hair(Enum):
    blonde = "blonde" 
    red = "red"
    brown = "brown"
    black = "black"
    grey = "grey"


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


class Riding_enums():
    gender = Enum("male", "female")
    #tribe_name_origin = random.choice(Tribe_name_origin)

eye_color = ('brown', 'black', 'blue', 'green', 'yellow')
hair_color = ('auburn', 'brown', 'black', 'blonde', 'copper', 'ginger', 'golden', 'grey', 'mouse', 'red', 'dark brown', 'white')
skin_tone = ('almond', 'brown', 'bronze', 'chocolate', 'cocoa', 'dark chocolate', 'fair', 'light', 'olive', 'pale', 'walnut')

rase_choice = ('Caucasian', 'Latino/Hispanic', 'African', 'Caribbean', 'Middle_Eastern', 'South_Asian', 'East_Asian', 'Mixed')

race_details = {
    'Europoidic' : {
        "Nordic" : {
            "Vzrůst" : random.choice("vysoký", "štíhlý"),
            "Postava" : "atletická (respiratorní), široká ramena, pevné držení těla",
            "Končetiny" : "dlouhé ruce a nohy",
            "Tělesná_výška" : "175",
            "Pigmentace" : "světle " + random.choice("bílá", "narůžovělá, jemná") + " pleť",
            "Nos" : "dlouhý, úzký, " + random.choice("rovný", "zahnutý"),
            "Rty" : "tenké",
            "Vlasy" : "světlé " + random.choice("jemné", "rovné", "vlnité") + " barvy "
                + random.choice("šedá", "myší", "zlatá", "blond", "bílá"),
            "Oči" : "světle " + random.choice("modré", "zelené", "šedé"),
            "Obličej" : "úzký, vysoký",
            "Brada" : random.choice("úzká", "hranatá", "ostrá"),
            "Lebka" : "dlouhá (dolichocefalie) – lebeční index 75-75,5, obličejový index nad 90",
            "Čelo" : "Ploché, úzké, dozadu sklopené ",
            "Čelist" : "dobře vyvinutá brada",
            "Oblast" : random.choice(
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
            )
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
            "Oblast" : random.choice(
                "Vestfálsko",
                "střední Švédsko"),
        },
        "Baltic" : {
            "Vzrůst" : random.choice("malý", "střední"),
            "Postava" : "podsaditá, rovná, široká ramena (digestivní)",
            "Končetiny" : "krátké",
            "Tělesná_výška" : "164",
            "Krk" : "široký, krátký",
            "Pigmentace" : random.choice("světlá", "žlutošedá"),
            "Nos" : random.choice("krátký", "mělký"),
            "Vlasy" : random.choice("pevné", "rovné") + random.choice("popelavé", "světlý blond"),
            "Oči" : random.choice("světle modré", "modrobílé") + "posazeny daleko od sebe, někdy i polo-mongoloidní tvar",
            "Obličej" : "robustní, široký, vysedlé lícní kosti",
            "Lebka" : "krátká (brachycefalie) – lebeční index 80,9-83,2 ",
            "Čelist" : "masivní s nevystupující bradou",
            "Brada" : random.choice("kulatá", "ustupující"),
            "Čelo" : "dozadu sklopené",
            "Oblast" : random.choice(
                "východní Evropa" 
                "střední a jižní Polsko",
                "Pobaltí " + random.choice("Litva", "Lotyšsko", "Estonsko"),
                "Česko",
                "Slovensko",
                "Maďarsko",
                "Ukrajina",
                "Bělorusko",
                "Finsko",
                "Rusko",
                "Skandinávie",
                "Holandsko",
            )
        },
        "Mediterran" : {
            "Vzrůst" : "nízký",
            "Postava" : "štíhlá (respiratorní), držení pružné",
            "Končetiny" : "v poměru k tělu dlouhé",
            "Tělesná_výška" : "161",
            "Pigmentace" : "hnědobílá",
            "Nos" : random.choice("rovný", "vysoký", "úzký") + "s vysokým hřbetem",
            "Rty" : "trochu výraznější oproti nordickému typu",
            "Vlasy" : "tmavé",
            "Čelo" : random.choice("více strmé a klenuté", "úzké"),
            "Oči" : "tmavě hnědé",
            "Obličej" : "oválný",
            "Brada" : "úzká",
            "Lebka" : "dlouhá (dolichocefalie) – lebeční index 70-75, obličejový index nad 90",
            "Oblast" : random.choice(
                "jižní a západní Evropa",
                "Středomoří",
                "Pádská nížina",
                "pobřeží Černého moře",
                "Španělsko",
                "Portugalsko", 
                "Řecko",
                "část Walesu",
                "Skotsko",
                "jižní Anglie a Irsko",
                "jihozápadní Německo",
                "jižní Polsko",
                "částečně jižní a centrální Rusko a Balkán",
            )
        },
        "Dinaric" : {
            "Vzrůst" : "vysoký",
            "Postava" : "štíhlá, astenická (respiratorní) s nenuceným držením těla",
            "Končetiny" : "dlouhé nohy, kratší ruce",
            "Tělesná_výška" : "174",
            "Krk" : "dlouhý",
            "Pigmentace" : random.choice("hnědobílá", "tmavší"),
            "Nos" : random.choice("velký", "úzký", "vysoký", "orlí (konvexní)"),
            "Vlasy" : "silné " + random.choice("tmavohnědé", "černé"),
            "Oči" : random.choice("tmavohnědé", "černé"),
            "Uši" : "velké",
            "Obličej" : "úzký, vystouplé lícní kosti",
            "Čelo" : "trochu dozadu sklopené",
            "Lebka" : "krátká (brachycefalie) se zploštělým, ale zakulaceným týlem – lebeční index 85-87, obličejový index 90-93",
            "Čelo" : "relativně vysoké, šikmé, rozvinuté nadočnicové oblouky",
            "Čelist" : "nevýrazná brada",
            "Brada" : random.choice("široká", "kulatá", "vysoká"),
            "Oblast" : random.choice(
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
            )
        },
        "Alpine" : {
            "Vzrůst" : "malý",
            "Tělesná_výška" : "163",
            "Postava" : "podsaditá (digestivní), těžkopádné",
            "Končetiny" : "krátké",
            "Pigmentace" : random.choice("žlutohnědá", "o něco tlustší"),
            "Nos" : random.choice("krátký" "tupý"),
            "Vlasy" : "tlusté, pevné " + random.choice("tmavohnědé", "černé"),
            "Oči" : "tmavohnědé",
            "Obličej" : "široký, kulatý",
            "Lebka" : "krátká (brachycefalie) – lebeční index 84-87, obličejový index nad 80",
            "Čelo" : random.choice("strmé", "klenuté", "kulaté", "široké"),
            "Čelist" : "široká",
            "Brada" : random.choice("tupá", "zaoblená"),
            "Oblast" : random.choice( 
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
            )
        }

    },
    'Middle_Eastern' : {
        'Hamitic' : {
            "Vzrůst" : "střední",
            "Postava" : "podsaditá (digestivní)",
            "Končetiny" : "krátké",
            "Pigmentace" : "snědá - barvy " + random.choice("mandle", "olivy", "vlašský ořech"),
            "Nos" : "zahnutý, masitý směrem dolů (podobá se číslici 6)",
            "Rty" : "masité, dolní ret je větší než horní",
            "Vlasy" : "tmavě " + random.choice("hnědé", "černé", "šedé") + ", kudrnaté, obočí často srostlé",
            "Oči" : "tmavě " + random.choice("hnědé", "černé", "zelené") + ", odhalená vrchní oční víčka (nevyvinuté nadočnicové oblouky)",
            "Uši" : "velké",
            "Obličej" : "středně široký, vystouplé lícní kosti",
            "Lebka" : "krátká (brachycefalie) se zploštělým týlem",
            "Čelo" : "nízké, šikmé, kulaté",
            "Čelist" : "nízká, ustupující brada",
            "Oblast" : random.choice(
                "Blízký východ (Malá Asie)",
                "Kavkaz",
                "Arménie",
                "Asýrie",
                "Ázerbájdžán",
                "Gruzie",
                "Libanon a Sýrie",
            )
        },
        'Sudeten' : {
            "Vzrůst": "malý",
            "Pigmentace": "tmavší - barvy " + random.choice("mandle", "olivy", "vlašský ořech"),
            "Nos": "široký, plochý",
            "Vlasy": "tmavě " + random.choice("hnědé", "černé", "šedé"),
            "Oči": "tmavě " + random.choice("hnědé", "zelené"),
            "Obličej": "středně široký, výrazné lícní kosti",
            "Lebka": "střední (mesocefalie)",
            "Čelist": "nevystupující brada",
            "Oblast": "východní Evropa",
        },
        'Oriental' : {
            "Vzrůst" : "malý až střední",
            "Postava" : "štíhlá (respiratorní)",
            "Pigmentace" : "snědá - barvy " + random.choice("mandle", "olivy", "vlašský ořech"),
            "Nos" : "úzký, vysoký",
            "Rty" : "plné",
            "Vlasy" : "tmavě " + random.choice("hnědé", "černé", "šedé"),
            "Oči" : "tmavě " + random.choice("hnědé", "černé", "zelené"),
            "Obličej" : "vysoký, převážně úzký a rovný",
            "Lebka" : "dlouhá (dolichocefalie)",
            "Oblast" : random.choice(
                "severní Afrika",
                "Blízký východ",
                "Arábie",
                "Libanon",
                "Irák",
                "Sýrie",
                "Turecko",
                "Degestán a Írán",
            )
    },
    'African' : {
        'Oriental' : {
            "Vzrůst" : "vysoký",
            "Postava" : "hodně astenická (respiratorní)",
            "Pigmentace" : "světle " + random.choice("čokoládová", "kakaová", "ořechová"),
            "Nos" : "rovný",
            "Rty" : "masité",
            "Vlasy" : "kudrnatě " + random.choice("hnědé", "černé", "šedé"),
            "Oči" : "tmavě "+ random.choice("hnědé", "černé"),
            "Obličej" : "vysoký",
            "Lebka" : "dlouhá (dolichocefalie)",
            "Oblast" : random.choice(
                "severní Afrika",
                "východní Afrika",
                "jižní Afrika",
            )
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
    'Mixed' : {
        "eye_color" : (eye_color),
        "hair_color" : (hair_color[1],hair_color[2],hair_color[7],hair_color[3],hair_color[9]),
        "skin_tone" : (skin_tone[9], skin_tone[6], skin_tone[7] ,skin_tone[2], skin_tone[2], skin_tone[8], skin_tone[3])
    }
}
}

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


print(random.choice(list(Tribe_name_origin)).value)

race_detail_type = random.choice(list(race_details))
print(race_detail_type)

# TODO: az po dodelani dat ras
if race_details['Europoidic']:
    None
    
print(race_detail_type, 'eye_color is : ', random.choice(race_details[race_detail_type]['eye_color']))
print(race_detail_type, 'hair_color is : ', random.choice(race_details[race_detail_type]['hair_color']))
print(race_detail_type, 'skin_tone is : ', random.choice(race_details[race_detail_type]['skin_tone']))

# gods_egypt.intent_gods_eg

print(random.choice(gods_egypt.intent_gods_eg))
x = len(gods_egypt.intent_gods_eg)
print(x)

if x in gods_egypt.intent_gods_about_eg:
    print(gods_egypt.intent_gods_about_eg[x])
