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
    runner = "runner"            #byvalej runner, nebo popripade i modifikace bodu na rozdeleni
    hero = "hero"              #mistni hrdina - mozno vice kontaktu, lepsi vztahy nekde - popripade i modifikace bodu na rozdeleni
    upper = "upper"
    middle = "middle"
    working = "working"
    priest = "priest"            #popripade shaman
    total_junkie = "total_junkie"      #totalni fetak
    homeless = "homeless"          #klasickej homeless chlast

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

rase_choice = ('Caucasian', 'Latino/Hispanic', 'African', 'Caribbean', 'Middle Eastern', 'South Asian', 'East Asian', 'Mixed')

#TODO: opravit hair slovnik a hair color - white a dark brown
# 1 means eye_color
# 2 means hair_color
# 3 means skin_tone
race_details = {
				'Europoidic' : {
					"eye_color" :   "light " + random.choice(eye_color),
					"hair_color" :  hair_color,
					"skin_tone" :   (skin_tone[9], skin_tone[10],skin_tone[8],skin_tone[7],skin_tone[2])
				},
				'Caucasian' : {
					"eye_color" : (eye_color[0], eye_color[2], eye_color[3]),
					"hair_color" : hair_color,
					"skin_tone" : (skin_tone[9], skin_tone[9],skin_tone[8],skin_tone[7],skin_tone[2])
				},
				'Latino/Hispanic' : {
					"eye_color" : (eye_color[0], eye_color[2], eye_color[3]), 
					"hair_color" : (hair_color[1],hair_color[2],hair_color[7]),
					"skin_tone" : (skin_tone[10], skin_tone[4], skin_tone[3],skin_tone[5], skin_tone[10])
				},
				'African' : {
					"eye_color" : (eye_color[0], eye_color[1]),
					"hair_color" : (hair_color[1],hair_color[2],hair_color[7]),
					"skin_tone" : (skin_tone[10], skin_tone[4],skin_tone[3],skin_tone[5])
				},
				'Caribbean' : {
					"eye_color" : (eye_color[0], eye_color[1],eye_color[3]),
					"hair_color" : (hair_color[1],hair_color[2],hair_color[7]),
					"skin_tone" : (skin_tone[10], skin_tone[4],skin_tone[3],skin_tone[5])
				},
				'Middle_Eastern' : {
					"eye_color" : (eye_color[0], eye_color[1],eye_color[3]),
					"hair_color" : (hair_color[1],hair_color[2],hair_color[7]),
					"skin_tone" : (skin_tone[10], skin_tone[8],skin_tone[1])
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

# RASA ŽLUTÁ
# VLASY: Rovné, černé
# •NOS: rovný, úzký,
# malý, nenápadný
# •OČI: šikmé, tmavé
# •OBLAST PŮVODU:
# Asie, Jižní Amerika
# •Např. Eskymáci a
# Indiáni

# NEGROIDNÍ
# ČERNÁ
# VLASY: kudrnaté,
# krátké, pomalu rostou
# NOS: široký, zploštělý
# OČI: velké, široké,
# tmavé
# OBLAST PŮVODU:
# subsaharská Afrika

# EUROPOIDNÍ
# BÍLÁ
# VLASY: mírně vlnité,
# různé barvy, rychle
# rostou
# NOS: rovný, úzký,
# zahnutý
# OČI: rovné, různé barvy
# OBLAST PŮVODU:
# Evropa, Severní Afrika
# a Západní Asie

# MÍŠENCI
#  MESTICI: bílá + žlutá rasa
#  MULATI: bílá + černá rasa
#  ZAMBOVÉ: černá + žlutá rasa
# Kastico beloch + indian + beloch
# Kajot mulat (cernoch + beloch) + mestic (beloch + indian)
# Kreolové: europoidní + negroidní
# Malgaši: negroidní + mongoloidní +
# tzv. australonéská rasa (uváděna jako 4.
# rasa – původní obyvatelé Austrálie)

# Bile plemeno
# alpinský
# • baltický
# • nordický
# • dinárský
# • mediteránní




# 6 Bílá – europoidní rasa
# Původní rozšíření: Evropa, Blízký východ, Střední východ, severní Afrika, Indie

# 7 Žlutohnědá – mongoloidní rasa
# Původní rozšíření: Asie, Amerika, Indonésie

# 8 Původní rozšíření: Afrika, Austrálie
# Černá – negroidní rasa
# Původní rozšíření: Afrika, Austrálie

# 9 Co bylo příčinou vzniku různých ras ?
# 10 Lidské rasy se vytvářely postupně před mnoha lety ze společných předků vlivem různého rozdílného prostředí.
# Těmto různým přírodním podmínkám se
# musely přizpůsobovat.
# (adaptovat se)

# 11 Co bylo příčinou jednotlivých odlišností ?
# tmavá pleť, tmavé oči
# štíhlá, vysoká postava
# ochrana před slunečním zářením
# větší povrch těla, rychle se zbavují tepla

# 12 menší, podsaditá postava
# úzká oční štěrbina
# menší, podsaditá postava
# oko chráněno před odrazem světla od sněhu, před mrazem
# menší povrch, méně se zbavují tepla, více tuku

# try it another way - more complex races

race_details = {
				'Europoidic' : {
					"Nordic" : {
                        "Vzrůst" : "vysoký",
                        "Postava" : "atletická (respiratorní), široká ramena",
                        "Končetiny" : "dlouhé ruce a nohy",
                        "Pigmentace" : "světle bílá",
                        "Nos" : "úzký, vysoký, rovný",
                        "Rty" : "tenké",
                        "Vlasy" : "světlé",
                        "Oči" : "světlé",
                        "Obličej" : "úzký, vysoký",
                        "Lebka" : "dlouhá (dolichocefalie) – lebeční index 75-75,5, obličejový index nad 90",
                        "Čelo" : "vysoké, rozvinuté nadočnicové oblouky",
                        "Čelist" : "dobře vyvinutá brada",
                        "Oblast" : (
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
                        "Oblast" : "nejčastěji v oblasti Vestfálska a částečně pak v severských zemí (střední Švédsko)",
                    },
                    "Baltic" : {
                        "Vzrůst" : "malý až střední",
                        "Postava" : "podsaditá, široká ramena (digestivní)",
                        "Končetiny" : "krátké",
                        "Krk" : "široký, krátký",
                        "Pigmentace" : "světle bílá",
                        "Nos" : "středně široký, nízký, prohlý (konkávní)",
                        "Vlasy" : "světlé",
                        "Oči" : "světlé, posazeny daleko od sebe, někdy i polo-mongoloidní tvar",
                        "Obličej" : "robustní, široký, vysedlé lícní kosti",
                        "Lebka" : "krátká (brachycefalie) – lebeční index 80,9-83,2 ",
                        "Čelist" : "Masivní s nevystupující bradou",
                        "Oblast" : (
                            "východní Evropa" 
                            "střední a jižní Polsko",
                            "Pobaltí (Litva, Lotyšsko, Estonsko)",
                            "Česko",
                            "Slovensko",
                            "Maďarsko",
                            "Ukrajina",
                            "Bělorusko",
                            "Finsko",
                            "Rusko",
                            "částečně ve Skandinávii a v Holandsku",
                        )
                    },
                    "Mediterran" : {
                        "Vzrůst" : "malý",
                        "Postava" : "štíhlá (respiratorní)",
                        "Končetiny" : "v poměru k tělu dlouhé",
                        "Pigmentace" : "hnědobílá",
                        "Nos" : "rovný, vysoký, úzký",
                        "Rty" : "trochu výraznější oproti nordickému typu",
                        "Vlasy" : "tmavé",
                        "Oči" : "tmavé",
                        "Obličej" : "oválný",
                        "Lebka" : "dlouhá (dolichocefalie) – lebeční index 70-75, obličejový index nad 90",
                        "Oblast" : (
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
                        "Postava" : "astenická (respiratorní)",
                        "Končetiny" : "dlouhé nohy, kratší ruce",
                        "Krk" : "dlouhý",
                        "Pigmentace" : "hnědobílá",
                        "Nos" : "úzký, vysoký, orlí (konvexní)",
                        "Vlasy" : "tmavé",
                        "Oči" : "tmavé",
                        "Uši" : "velké",
                        "Obličej" : "úzký, vystouplé lícní kosti",
                        "Lebka" : "krátká (brachycefalie) se zploštělým, ale zakulaceným týlem – lebeční index 85-87, obličejový index 90-93",
                        "Čelo" : "relativně vysoké, šikmé, rozvinuté nadočnicové oblouky",
                        "Čelist" : "nevýrazná brada",
                        "Oblast" : (
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
                    }
                },
                'Middle_Eastern' : {
                    'Armenoidic' : {
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
                        "Oblast" : (
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
                        "Oblast" : (
                            "severní Afrika",
                            "Blízký východ",
                            "Arábie",
                            "Libanon",
                            "Irák",
                            "Sýrie",
                            "Turecko",
                            "Degestán a Írán",
                        )
                }
            }

                eye_color = ('brown', 'black', 'blue', 'green', 'yellow')
                ('brown', 'black', 'green')
                ("hnědé", "černé", "zelené")
hair_color = ('auburn', 'brown', 'black', 'blonde', 'copper', 'ginger', 'golden', 'grey', 'mouse', 'red', 'dark brown', 'white')
('brown', 'black', 'grey',)
("hnědé", "černé", "šedé",)
skin_tone = ('almond', 'brown', 'bronze', 'chocolate', 'cocoa', 'dark chocolate', 'fair', 'light', 'olive', 'pale', 'walnut')
('almond', 'olive', 'walnut')
("mandle", "olivy", "vlašský ořech")




