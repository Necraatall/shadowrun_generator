from enum import Enum, auto
from random import *

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
    "sexy"
    "handsome"
    "beautiful"
    "tall"
    "short"

class Social_class(Enum):
    "runner"
    "hero"
    "upper"
    "middle"
    "working"
    "total_junkie"      #totalni fetak
    "homeless"          #klasickej homeless chlast

class Positive_characteristic(Enum):
    "creative"
    "brave"
    "smart"
    "exciting"
    "energetic"
    "entertaining"
    "inspiring"
    "gentle"
    "friendly"
    "generous"
    "considerate"
    "bright"
    "kind"
    "giving"
    "loveable"
    "stable"

class Negative_characteristic(Enum):
    "disloyal"
    "sneaky"
    "untrustworthy"
    "cowardly"
    "unintelligent"
    "dull"
    "boring"
    "lazy"
    "rude"
    "unkind"
    "standoffish"
    "unfriendly"
    "stingy"
    "greedy"
    "selfish"
    "violent"
    "unstable"
    "sadistic"
    "evil"

# na zaklade tohoto je mozne resit ze jej nekdo sikanoval ci si na nej nedovolili
class Height(Enum):
	"very tall"
	"tall"
	"average"
	"short"
	"very short"

class Weight(Enum):
	"very overweight"
	"overweight"
	"average"
	"underweight"
	"very underweight"

class Build(Enum):
	"very well-built"
	"well-built"
	"average build"
	"fine build"
	"very fine build"

class Hair(Enum):
    "blonde" 
    "red"
    "brown"
    "black"
    "grey"


#TODO: TOTO: mozna do jineho souboru
class Nationality(Enum):
    'Afghan'
    'Argentinian'
    'Spanish'
    'Australian'
    'British'
    'American'
    'Belgian'
    'Brazilian'
    'Welsh'
    'Portuguese'
    'Canadian'
    'French'
    'English'
    'Scottish'
    'Irish'
    'Cornish'
    'Colombian'
    'Danish'
    'Egyptian'
    'Ethiopian'
    'Finnish'
    'German'
    'Greek'
    'Italian'
    'Japanese'
    'Mexican'
    'Dutch'
    'Swedish'
    'Thai'
    'Polish'
    'Hungarian'
    'Czech'
    'Slovak'
    'Austrian'
    'Ukrain'
    'Slovenian'
    'Hrvat'
    'Monte Negro'
    'Rusian'
    'Chinees'
  

class Riding_enums():
    gender = Enum("male", "female")
    #tribe_name_origin = random.choice(Tribe_name_origin)



eye_color = ['brown', 'black', 'blue', 'green', 'yellow']
hair_color = ['auburn', 'brown', 'black', 'blonde', 'copper', 'ginger', 'golden', 'grey', 'mouse', 'red']
skin_tone = ['almond', 'brown', 'bronze', 'chocolate','cocoa', 'dark chocolate', 'fair', 'light', 'olive', 'pale', 'olive', 'walnut']

rase_choice = ['Caucasian', 'Latino/Hispanic', 'African', 'Caribbean', 'Middle Eastern', 'South Asian', 'East Asian', 'Mixed']

# 1 means eye_color
# 2 means hair_color
# 3 means skin_tone
race_details = {
				'Caucasian' : {
					1 : [eye_color[0], eye_color[2], eye_color[3]],
					2 : hair_color,
					3 : [skin_tone[9], skin_tone[10],skin_tone[8],skin_tone[7],skin_tone[2]]
				},
				'Latino/Hispanic' : {
					1 : [[eye_color[0], eye_color[2], eye_color[3]]], 
					2 : [hair_color[1],hair_color[2],hair_color[7]],
					3 : [skin_tone[11], skin_tone[4], skin_tone[3],skin_tone[5], skin_tone[10]]

				},
				'African' : {
					1 : [[eye_color[0], eye_color[1]]],
					2 : [hair_color[1],hair_color[2],hair_color[7]],
					3 : [skin_tone[11], skin_tone[4],skin_tone[3],skin_tone[5]]
				},
				'Caribbean' : {
					1 : [[eye_color[0], eye_color[1],eye_color[3]]],
					2 : [hair_color[1],hair_color[2],hair_color[7]],
					3 : [skin_tone[11], skin_tone[4],skin_tone[3],skin_tone[5]]
				},
				'Middle Eastern' : {
					1 : [[eye_color[0], eye_color[1],eye_color[3]]],
					2 : [hair_color[1],hair_color[2],hair_color[7]],
					3 : [skin_tone[11], skin_tone[8],skin_tone[1]]
				},
				'South Asian' : {
					1 : [[eye_color[0], eye_color[1]]],
					2 : [hair_color[1],hair_color[2],hair_color[7]],
					3 : [skin_tone[11], skin_tone[8],skin_tone[1]]
				},
				'East Asian' : {
					1 : [[eye_color[0], eye_color[1]]],
					2 : ['dark brown', hair_color[2],hair_color[7], 'white'],
                    3 : [skin_tone[9], skin_tone[6], skin_tone[7] ,skin_tone[1]]
				},
				'Mixed' : {
					1 : [eye_color],
                    2 : [hair_color[1],hair_color[2],hair_color[7],hair_color[3],hair_color[9]],
                    3 : [skin_tone[9], skin_tone[6], skin_tone[7] ,skin_tone[2], skin_tone[2], skin_tone[8], skin_tone[3]]
				}
			}
