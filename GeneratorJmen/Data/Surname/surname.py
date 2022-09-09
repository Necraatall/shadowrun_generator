import random

from GeneratorJmen.Data.Surname.surname_cz import *
from GeneratorJmen.Data.Surname.surname_cn import *
from GeneratorJmen.Data.Surname.surname_de import *
from GeneratorJmen.Data.Surname.surname_es import *
from GeneratorJmen.Data.Surname.surname_fr import *
from GeneratorJmen.Data.Surname.surname_gk import *
from GeneratorJmen.Data.Surname.surname_hi import *
from GeneratorJmen.Data.Surname.surname_ie import *
from GeneratorJmen.Data.Surname.surname_il import *
from GeneratorJmen.Data.Surname.surname_it import *
from GeneratorJmen.Data.Surname.surname_kr import *
from GeneratorJmen.Data.Surname.surname_ne import *
from GeneratorJmen.Data.Surname.surname_pl import *
from GeneratorJmen.Data.Surname.surname_pt import *
from GeneratorJmen.Data.Surname.surname_ru import *
from GeneratorJmen.Data.Surname.surname_uk import *
from GeneratorJmen.Data.Surname.surname_us import *

surnames_all = [
    intent_surname_cz,
    intent_surname_cn,
    intent_surname_de,
    intent_surname_es,
    intent_surname_fr,
    intent_surname_gk,
    intent_surname_hi,
    intent_surname_ie,
    intent_surname_it,
    intent_surname_kr,
    intent_surname_ne,
    intent_surname_pl,
    intent_surname_pt,
    intent_surname_ru,
    intent_surname_uk,
    intent_surname_us
]


class Surname:
    @staticmethod
    def get_random_tribe_surname():
        return get_random_surname()


def get_random_surname():
    return random.choice(random.choice(surnames_all))
