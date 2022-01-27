from GeneratorJmen.jmeno_all import *
from GeneratorJmen.surname_slavic import *
from GeneratorJmen.surname_chinees import *
import random

class generator_celeho_jmena:
    chosen_name = random.choice(intent_name_all)
    print(chosen_name)
    intent_tribe_backround = [
        intent_surname_slavic,
        intent_surname_chinees
    ]
    chosen_surname = random.choice(intent_tribe_backround)
    print(chosen_name + " " + chosen_surname)
