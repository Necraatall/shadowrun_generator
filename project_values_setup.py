from enum import Enum, auto
from random import *


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



class Riding_enums():
    gender = Enum("male", "female")
    tribe_name_origin = random.choice(Tribe_name_origin)
