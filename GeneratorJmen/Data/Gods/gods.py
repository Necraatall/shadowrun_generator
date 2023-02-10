import random
from ..Gods.gods_egypt import *
from ..Gods.gods_greek import *
from ..Gods.gods_kelt import *
from ..Gods.gods_slovan import *

INTENT_TRIBE_GOD = (
    GODS_EG,
    GODS_GK,
    GODS_KELT,
    GODS_SLOVAN,
)

class God:
    @staticmethod
    def get_random_tribe_god_with_abouts():
        return get_random_god_with_abouts()


def get_random_god_with_abouts():
    # vyber list uvnitr listu INTENT_TRIBE_GOD - nevybere jmeno, ale hodnoty
    chosen_god = random.choice(INTENT_TRIBE_GOD)
    chosen_god = str(chosen_god)[1:-1]
    # odeslu jmeno boha a popis boha
    return chosen_god
