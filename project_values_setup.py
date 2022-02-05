from enum import Enum, auto


class Gender(Enum):
    male   = auto()
    female = auto()

class Tribe_name_origin(Enum):
    cz = auto()
    pl = auto()
    ne = auto()
    es = auto()
    fr = auto()
    gk = auto()
    it = auto()
    us = auto()

class Tribe_surname_origin(Enum):
    cz = auto()
    pl = auto()
    ne = auto()
    es = auto()
    fr = auto()
    gk = auto()
    it = auto()
    us = auto()

#nutno dovymyslet dalsi, aby jsme s nimi i mohli pocitat jinde
class Physical_characteristic(Enum):
	sexy = auto()
	handsome = auto()
	beautiful = auto()
	tall = auto()
	short = auto()

class Social_class(Enum):
    runner = auto()
    hero = auto()
    upper = auto()
    middle = auto()
    working = auto()
    total_junkie = auto()       #totalni fetak
    homeless = auto()           #klasickej homeless chlast

class Positive_characteristic(Enum):
    creative = auto()
    brave = auto()
    smart = auto()
    exciting = auto()
    energetic = auto()
    entertaining = auto()
    inspiring = auto()
    gentle = auto()
    friendly = auto()
    generous = auto()
    considerate = auto()
    bright = auto()
    kind = auto()
    giving = auto()
    loveable = auto()
    stable = auto()

class Negative_characteristic(Enum):
    disloyal = auto()
    sneaky = auto()
    untrustworthy = auto()
    cowardly = auto()
    unintelligent = auto()
    dull = auto()
    boring = auto()
    lazy = auto()
    rude = auto()
    unkind = auto()
    standoffish = auto()
    unfriendly = auto()
    stingy = auto()
    greedy = auto()
    selfish = auto()
    violent = auto()
    unstable = auto()
    sadistic = auto()
    evil = auto()

# na zaklade tohoto je mozne resit ze jej nekdo sikanoval ci si na nej nedovolili
class Height():
	very_tall = auto()
	tall = auto()
	average = auto()
	short = auto()
	very_short = auto()

#TODO: weight atd.