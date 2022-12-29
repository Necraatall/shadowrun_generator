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
skin_tone = ('almond', 'brown', 'bronze', 'chocolate','cocoa', 'dark chocolate', 'fair', 'light', 'olive', 'pale', 'olive', 'walnut')

rase_choice = ('Caucasian', 'Latino/Hispanic', 'African', 'Caribbean', 'Middle Eastern', 'South Asian', 'East Asian', 'Mixed')

#TODO: opravit hair slovnik a hair color - white a dark brown
# 1 means eye_color
# 2 means hair_color
# 3 means skin_tone
race_details = {
				'Caucasian' : {
					"eye_color" : (eye_color[0], eye_color[2], eye_color[3]),
					"hair_color" : hair_color,
					"skin_tone" : (skin_tone[9], skin_tone[10],skin_tone[8],skin_tone[7],skin_tone[2])
				},
				'Latino/Hispanic' : {
					"eye_color" : (eye_color[0], eye_color[2], eye_color[3]), 
					"hair_color" : (hair_color[1],hair_color[2],hair_color[7]),
					"skin_tone" : (skin_tone[11], skin_tone[4], skin_tone[3],skin_tone[5], skin_tone[10])
				},
				'African' : {
					"eye_color" : (eye_color[0], eye_color[1]),
					"hair_color" : (hair_color[1],hair_color[2],hair_color[7]),
					"skin_tone" : (skin_tone[11], skin_tone[4],skin_tone[3],skin_tone[5])
				},
				'Caribbean' : {
					"eye_color" : (eye_color[0], eye_color[1],eye_color[3]),
					"hair_color" : (hair_color[1],hair_color[2],hair_color[7]),
					"skin_tone" : (skin_tone[11], skin_tone[4],skin_tone[3],skin_tone[5])
				},
				'Middle Eastern' : {
					"eye_color" : (eye_color[0], eye_color[1],eye_color[3]),
					"hair_color" : (hair_color[1],hair_color[2],hair_color[7]),
					"skin_tone" : (skin_tone[11], skin_tone[8],skin_tone[1])
				},
				'South Asian' : {
					"eye_color" : (eye_color[0], eye_color[1]),
					"hair_color" : (hair_color[1],hair_color[2],hair_color[7]),
					"skin_tone" : (skin_tone[11], skin_tone[8],skin_tone[1])
				},
				'East Asian' : {
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
print(race_detail_type, 'eye_color is : ', random.choice(race_details[race_detail_type]['eye_color']))
print(race_detail_type, 'hair_color is : ', random.choice(race_details[race_detail_type]['hair_color']))
print(race_detail_type, 'skin_tone is : ', random.choice(race_details[race_detail_type]['skin_tone']))

# gods_egypt.intent_gods_eg

print(random.choice(gods_egypt.intent_gods_eg))
x=random.choice(len(gods_egypt.intent_gods_eg))
if x in gods_egypt.intent_gods_about_eg:
    print(gods_egypt.intent_gods_about_eg[x])
