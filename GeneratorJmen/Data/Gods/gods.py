import random
from ..Gods.gods_egypt import *
from ..Gods.gods_greek import *
from ..Gods.gods_kelt import *
from ..Gods.gods_slovan import *

intent_tribe_god = (
    intent_gods_eg,
    intent_gods_about_gk,
    intent_gods_kelt,
    intent_gods_slovan,
)

intent_tribe_god_about = (
    intent_gods_about_eg,
    intent_gods_about_gk,
    intent_gods_about_kelt,
    intent_gods_about_slovan,
)


class God:
    @staticmethod
    def get_random_tribe_god_with_abouts():
        return get_random_god_with_abouts()


def get_random_god_with_abouts():
    # vyber list uvnitr listu intent_tribe_god - nevybere jmeno, ale hodnoty
    chosen_list = random.choice(intent_tribe_god)
    # vyber index listu pro pozdejsi pouziti
    get_index_of_tribes_god = intent_tribe_god.index(chosen_list)

    # vybere jednoho boha z listu bohu dle indexu ziskaneho vyse
    chosen_god = random.choice(intent_tribe_god[get_index_of_tribes_god])
    # vybere index vybraneho boha
    get_index_of_god = intent_tribe_god[get_index_of_tribes_god].index(chosen_god)

    # rozsekam vystup na jmeno boha a jeho popis kdy si vemu jen popis
    # vemu si hodnotu popisu boha a dam do stringu
    split_output_chosen_god_about = str(intent_tribe_god_about[get_index_of_tribes_god][get_index_of_god])
    # osetrim aby hodnota nemela nechtene zvlastni znaky
    split_output_chosen_god_about = split_output_chosen_god_about[5:][:-2].replace("'", "")
    # odeslu jmeno boha a popis boha
    return chosen_god, split_output_chosen_god_about
