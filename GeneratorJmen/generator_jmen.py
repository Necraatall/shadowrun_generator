from GeneratorJmen.Data.jmeno_all import *
from GeneratorJmen.Data.surname_cz import *
from GeneratorJmen.Data.surname_cn import *
from GeneratorJmen.Data.surname_de import *
from GeneratorJmen.Data.surname_es import *
from GeneratorJmen.Data.surname_eus import *
from GeneratorJmen.Data.surname_fr import *
from GeneratorJmen.Data.surname_gk import *
from GeneratorJmen.Data.surname_hi import *
from GeneratorJmen.Data.surname_ie import *
from GeneratorJmen.Data.surname_il import *
from GeneratorJmen.Data.surname_it import *
from GeneratorJmen.Data.surname_kr import *
from GeneratorJmen.Data.surname_ne import *
from GeneratorJmen.Data.surname_pl import *
from GeneratorJmen.Data.surname_pt import *
from GeneratorJmen.Data.surname_ru import *
from GeneratorJmen.Data.surname_uk import *
from GeneratorJmen.Data.surname_us import *

import random

class surname_rand:
    @staticmethod
    def list_of_intents_tribe_backround():
        #TODO dodelat prijmeni
        intent_tribe_backround = [
            intent_surname_cz,
            intent_surname_cn,
            intent_surname_de,
            intent_surname_es,
            intent_surname_eus,
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
        chosen_surname = random.choice(intent_tribe_backround)
        return chosen_surname

class generator_celeho_jmena:
    chosen_name = random.choice(intent_name_all)
    #print(chosen_name)
    #print(str(random.choice(surname_rand.list_of_intents_tribe_backround())))
    print(chosen_name + " " + str(random.choice(surname_rand.list_of_intents_tribe_backround())))
