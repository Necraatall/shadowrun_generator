from GeneratorJmen.jmeno_all import *
from GeneratorJmen.surname_cz import *
from GeneratorJmen.surname_cn import *
from GeneratorJmen.surname_de import *
from GeneratorJmen.surname_es import *
from GeneratorJmen.surname_eus import *

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
            intent_surname_eus
        ]
        chosen_surname = random.choice(intent_tribe_backround)
        return chosen_surname

class generator_celeho_jmena:
    chosen_name = random.choice(intent_name_all)
    #print(chosen_name)
    #print(str(random.choice(surname_rand.list_of_intents_tribe_backround())))
    print(chosen_name + " " + str(random.choice(surname_rand.list_of_intents_tribe_backround())))
