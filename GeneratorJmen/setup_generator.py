from operator import index
from GeneratorJmen.Data.Name.jmeno_all import *
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

from GeneratorJmen.Data.Name.names_gk import *
from GeneratorJmen.Data.Name.names_fi import *
from GeneratorJmen.Data.Name.names_pl import *
from GeneratorJmen.Data.Name.names_it import *
from GeneratorJmen.Data.Name.names_no import *
from GeneratorJmen.Data.Name.names_ne import *
from GeneratorJmen.Data.Name.names_se import *
from GeneratorJmen.Data.Name.names_hu import *
from GeneratorJmen.Data.Name.names_us import *
from GeneratorJmen.Data.Name.names_sk import *
from GeneratorJmen.Data.Name.names_fr import *
from GeneratorJmen.Data.Name.names_es import *
from GeneratorJmen.Data.Name.names_vn import *

from GeneratorJmen.Data.NickName.nicknames_cz import *

from GeneratorJmen.Data.Gods.gods_greek import *
from GeneratorJmen.Data.Gods.gods_egypt import *
from GeneratorJmen.Data.Gods.gods_kelt import *
from GeneratorJmen.Data.Gods.gods_slovan import *

import random




class surname_rand:
    @staticmethod
    def list_of_intents_tribe_surname():
        intent_tribe_surname = [
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
        chosen_surname = random.choice(random.choice(intent_tribe_surname))
        return chosen_surname

class name_rand:
    @staticmethod
    def list_of_intents_tribe_names():
        intent_tribe_name = [
            intent_names_gk,
            intent_names_fi,
            intent_names_pl,
            intent_names_it,
            intent_names_no,
            intent_names_ne,
            intent_names_se,
            intent_names_hu,
            intent_names_us,
            intent_names_sk,
            intent_names_fr,
            intent_names_es,
            intent_names_vn
            
        ]
        chosen_name = random.choice(random.choice(intent_tribe_name))
        return chosen_name

class nickName_rand:
    @staticmethod
    def list_of_intents_tribe_nickNames():
        intent_tribe_nickName = [
            intent_nickNames_cz
            
        ]
        chosen_nickName = random.choice(random.choice(intent_tribe_nickName))
        return chosen_nickName

class god_rand:
    @staticmethod
    def list_of_intents_tribe_gods():
        intent_tribe_god = [
            intent_gods_gk,
            intent_gods_eg,
            intent_gods_kelt,
            intent_gods_slovan

        ]

        intent_tribe_god_about = [
            intent_gods_about_gk,
            intent_gods_about_eg,
            intent_gods_about_kelt,
            intent_gods_about_slovan

        ]


        #vyber list uvnitr listu intent_tribe_god - nevybere jmeno, ale hodnoty
        chosen_list = random.choice(intent_tribe_god)
        #vyber index listu pro pozdejsi pouziti
        get_index_of_tribes_god = intent_tribe_god.index(chosen_list)

        #vybere jednoho boha z listu bohu dle indexu ziskaneho vyse
        chosen_god = random.choice(intent_tribe_god[get_index_of_tribes_god])
        #vybere index vybraneho boha
        get_index_of_god = intent_tribe_god[get_index_of_tribes_god].index(chosen_god)

        #rozsekam vystup na jmeno boha a jeho popis kdy si vemu jen popis
        #vemu si hodnotu popisu boha a dam do stringu 
        split_output_chosen_god_about = str(intent_tribe_god_about[get_index_of_tribes_god][get_index_of_god])
        #osetrim aby hodnota nemela nechtene zvlastni znaky
        split_output_chosen_god_about = split_output_chosen_god_about[5:][:-2].replace("'","")
        # odeslu jmeno boha a popis boha
        return chosen_god, split_output_chosen_god_about
