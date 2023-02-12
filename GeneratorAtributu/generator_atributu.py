"""
    High level: kod dokaze vygenerovat atributy, ovlivnit rasou, zapsat do atributes_dict (vcetne Magie a resonance) a vypsat je
    Deep level: kod vyrandomuje zda dotycny je magic/resonance user (a odecte je ze zbyvajicich Pointspool)
                kod vybere z ktereho listu hodnot bude pridelovat hodnoty do atributu
                kod vybere hodnoty a priradi
                kod vybere rasu a modifikuje hodnoty atributu o jeji minima a maxima
                kod vypise hodnoty do terminalu a ulozi je docasne do slovniku
    Deepest level:  kod potrebuje mit hodnotu pointspool - je to pocet bodu na celou postavu
                    kod si zjisti hodnotu poctu bodu pro generovani atributu - pointspool_atr_start (polovina pointspool) a pripocte k ni 80 (za kazdy atribut 10)
                    kod prida hodnotu 5 ke skill bodum, paklize zustal zbytek diky lichemu poctu cisel 6
                    kod si randomizuje zda je magic user, pokud ano, tak vygeneruje mu hodnotu k atributu Magic/Reason, zapise jej do dict a listu
                    kod zjisti si kolik bodu ma na skilly a vygeneruje si jeden list z ktereho bude plnit random nepouzity atribut (100, 200, 250, 300, 425 a vice do hodnoty 600)
                    kod si zavola meta cast - rasy, a upravi hodnoty v dict i v listech
                    kod vypise vysledek

"""
import random
from dataclasses import dataclass
from typing import Dict
from collections import OrderedDict


# základní list s atributy, ze kterého se vybírá
LISTATR = ['Body', 'Agility', 'Reaction', 'Strength', 'Charisma', 'Intuition', 'Logic', 'Willpower']
usedatr = LISTATR
LISTATR = list(LISTATR)
RACE_DICT: dict = {}
final_atributes: dict= {}
chosed_tuple: tuple = ()
# choose_destiny = None   # 96 - 100 is full Thaumaturgic, 91-95 is full shamanic, 86-90 is Thaumaturgy Adept, 81-85 is Shamanic Adept, 75-80 is Technomancer  
# is_mage = None          # 10 is full Thaumaturgic, 9 is full shamanic, 8 is Thaumaturgy Adept, 7 is Shamanic Adept, 6 physical Adept, 7 is Technomancer 

HUMAN_RACE_DICT = {
    'BS': 0,
    'Metatype': "Human",
    'Body':         (1, 6, 9, 0),
    'Agility':      (1, 6, 9, 0),
    'Reaction':     (1, 6, 9, 0),
    'Strength':     (1, 6, 9, 0),
    'Charisma':     (1, 6, 9, 0),
    'Intuition':    (1, 6, 9, 0),
    'Logic':        (1, 6, 9, 0),
    'Willpower':    (1, 6, 9, 0),
    'Initiative':   (2, 12, 18),
    'Edge':         (2, 7, 10, 1),
    'Initiative_Phases': 1,
    'Metatype Ability': "+1 Edge"
}

ORC_RACE_DICT = {
    'BS': 20,
    'Metatype': "Orc",
    'Body':         (4, 9, 13, 3),
    'Agility':      (1, 6, 9, 0),
    'Reaction':     (1, 6, 9, 0),
    'Strength':     (3, 8, 12, 2),
    'Charisma':     (1, 5, 7, -1),
    'Intuition':    (1, 6, 9, 0),
    'Logic':        (1, 5, 7, -1),
    'Willpower':    (1, 6, 9, 0),
    'Initiative':   (2, 12, 18),
    'Edge':         (1, 6, 9, 0),
    'Initiative_Phases': 1,
    'Metatype Ability': "Low-Light Vision"
}

DWARF_RACE_DICT = {
    'BS': 25,
    'Metatype': "Dwarf",
    'Body':         (2, 7, 10, 1),
    'Agility':      (1, 6, 9, 0),
    'Reaction':     (1, 5, 7, -1),
    'Strength':     (3, 8, 12, 2),
    'Charisma':     (1, 6, 9, 0),
    'Intuition':    (1, 6, 9, 0),
    'Logic':        (1, 6, 9, 0),
    'Willpower':    (2, 7, 10, 0),
    'Initiative':   (2, 11, 16),
    'Edge':         (1, 6, 9, 0),
    'Initiative_Phases': 1,
    'Metatype Ability': "Thermographic Vision, +2 dice for Body Tests to resist pathogens and toxins"
}

ELF_RACE_DICT = {
    'BS': 30,
    'Metatype': "Elf",
    'Body':         (1, 6, 9, 0),
    'Agility':      (2, 7, 10, 1),
    'Reaction':     (1, 6, 9, 0),
    'Strength':     (1, 6, 9, 0),
    'Charisma':     (3, 8, 12, 2),
    'Intuition':    (1, 6, 9, 0),
    'Logic':        (1, 6, 9, 0),
    'Willpower':    (1, 6, 9, 0),
    'Initiative':   (2, 12, 18),
    'Edge':         (1, 6, 9, 0),
    'Initiative_Phases': 1,
    'Metatype Ability': "Low-Light Vision"
}

TROLL_RACE_DICT = {
    'BS': 40,
    'Metatype': "Troll",
    'Body':         (5, 10, 15, 4),     # 5
    'Agility':      (1, 5, 7, -1),      # 5
    'Reaction':     (1, 6, 9, 0),       # 5
    'Strength':     (5, 10, 15, 4),     # 5
    'Charisma':     (1, 4, 6, -2),      # 5
    'Intuition':    (1, 5, 7, -1),      # 5
    'Logic':        (1, 5, 7, -1),      # 5
    'Willpower':    (1, 6, 9, 0),       # 4
    'Initiative':   (2, 11, 16),
    'Edge':         (1, 6, 9, 1),
    'Initiative_Phases': 1,
    'Metatype Ability': "Thermographic Vision, +1 Reach, +1 natural armor (cumulative with worn armor)"
}

# this one is prepared for the future
metahuman_race_list = ['Human', 'Orc', 'Dwarf', 'Elf', 'Troll']


class Atributes():

    def make_atributes():
        # TODO: definovat nekde nahore ci uplne bokem body pres promennou
        # pointspool celkovy pocet bodu na postavu
        pointspool: int
        # pointspool_skills pocet bodu na skilly, Edge, rasu, Merits and Flows (neg: critters)
        pointspool_skills: int  # na platbu za edge, rasu a skilly
        # pointspool_atr_start kolik je do zacatku max na atributy - zde rozdeluji vsechny body ktere lze zakoupit (muze
        pointspool_atr_start: int  # na vypocet atributu vcetne bonusu rasy
        # adventages celkovy pocet bodu na obdareni a postizeni
        adventages: int
        # pointspool/2 must be [200, 300, 340, 390, 400, 430, 440, 500, 600, 640, 690]
        pointspool = random.choice((200, 300, 340, 390, 400, 430, 440, 500, 600, 640, 690))
        # TODO: better way for counting atributes and so one but there is realy huge pool of skils
        pointspool_atr_start = round((pointspool/2) + (len(usedatr) * 10))
        pointspool_skills = pointspool - pointspool_atr_start + adventages
        match pointspool_atr_start:
            case 180:  # 100BP
                atribute_pool = {
                    1: (4, 4, 2, 2, 2, 2, 1, 1),
                    2: (4, 3, 3, 3, 2, 1, 1, 1),
                    3: (4, 3, 3, 2, 2, 2, 1, 1),
                    4: (4, 3, 2, 2, 2, 2, 2, 1),
                    5: (4, 2, 2, 2, 2, 2, 2, 2),
                    6: (3, 3, 3, 3, 3, 1, 1, 1),
                    7: (3, 3, 3, 3, 2, 2, 1, 1),
                    8: (3, 3, 3, 2, 2, 2, 2, 1),
                    9: (3, 3, 2, 2, 2, 2, 2, 2),
                }
                chosed_tuple = atribute_pool[random.randint(1, len(atribute_pool))]

            case 230:  # 150BP
                atribute_pool = {
                    1: (5, 5, 4, 3, 3, 2, 1, 1),
                    2: (5, 4, 4, 3, 3, 2, 1, 1),
                    3: (5, 4, 4, 3, 2, 2, 2, 1),
                    4: (5, 4, 4, 2, 2, 2, 2, 2),
                    5: (5, 4, 3, 3, 3, 3, 1, 1),
                    6: (5, 4, 3, 3, 3, 2, 2, 1),
                    7: (5, 4, 3, 3, 2, 2, 2, 2),
                    8: (5, 3, 3, 3, 3, 3, 2, 1),
                    9: (5, 3, 3, 3, 3, 2, 2, 2),
                    10: (4, 4, 4, 3, 3, 3, 1, 1),
                    11: (4, 4, 4, 3, 3, 2, 2, 1),
                    12: (4, 4, 4, 3, 2, 2, 2, 2),
                    13: (4, 4, 3, 3, 3, 3, 2, 1),
                    14: (4, 4, 3, 3, 3, 2, 2, 2),
                    15: (4, 3, 3, 3, 3, 3, 3, 1),
                    16: (4, 3, 3, 3, 3, 3, 2, 2),
                    17: (3, 3, 3, 3, 3, 3, 3, 2),
                }
                chosed_tuple = atribute_pool[random.randint(1, len(atribute_pool))]
            case 250:  # 170BP
                atribute_pool = {
                    1: (5, 5, 3, 3, 3, 2, 2, 2),
                    2: (5, 4, 4, 3, 3, 2, 2, 2),
                    3: (5, 4, 4, 3, 3, 3, 2, 1),
                    4: (5, 4, 4, 3, 3, 2, 2, 2),
                    5: (5, 4, 3, 3, 3, 3, 2, 2),
                    6: (5, 5, 4, 4, 2, 2, 2, 1),
                    7: (5, 5, 5, 2, 2, 2, 2, 2),
                    8: (5, 3, 3, 3, 3, 3, 3, 2),
                    10: (4, 4, 4, 3, 3, 3, 2, 2),
                    13: (4, 4, 3, 3, 3, 3, 3, 2),
                    14: (4, 3, 3, 3, 3, 3, 3, 3),
                }
                chosed_tuple = atribute_pool[random.randint(1, len(atribute_pool))]
            case 275:  # 195 BP
                atribute_pool = {
                    1: (6, 5, 4, 3, 3, 3, 1, 1),
                    2: (6, 5, 4, 3, 2, 2, 2, 2),
                    3: (6, 5, 4, 4, 3, 2, 1, 1),
                    4: (6, 5, 4, 3, 3, 3, 1, 1),
                    5: (6, 5, 4, 3, 2, 2, 2, 2),
                    6: (6, 5, 3, 3, 3, 3, 2, 1),
                    7: (6, 4, 4, 3, 3, 3, 2, 1),
                    8: (6, 4, 3, 3, 3, 3, 3, 1),
                    9: (6, 3, 3, 3, 3, 3, 3, 2),
                    }
                chosed_tuple = atribute_pool[random.randint(1, len(atribute_pool))]
            case 280:  # 200 BP
                atribute_pool = {
                    1: (5, 5, 4, 4, 4, 3, 2, 1),
                    2: (5, 5, 4, 4, 3, 3, 3, 1),
                    3: (5, 5, 4, 4, 3, 3, 2, 2),
                    4: (5, 5, 4, 3, 3, 3, 3, 2),
                    5: (5, 4, 4, 4, 3, 3, 3, 2),
                    6: (5, 4, 4, 3, 3, 3, 3, 3),
                    7: (4, 4, 4, 4, 3, 3, 3, 3),
                    8: (4, 4, 4, 4, 4, 4, 2, 2),
                    10: (4, 4, 4, 4, 4, 3, 3, 2),
                }
                chosed_tuple = atribute_pool[random.randint(1, len(atribute_pool))]

            case 295:  # 215 BP
                atribute_pool = {
                    1: (6, 5, 4, 4, 4, 3, 2, 1),
                    2: (6, 5, 4, 4, 3, 3, 3, 1),
                    3: (6, 5, 4, 4, 3, 3, 2, 2),
                    4: (6, 5, 4, 3, 3, 3, 3, 2),
                    5: (6, 4, 4, 4, 3, 3, 3, 2),
                    6: (6, 4, 4, 3, 3, 3, 3, 3),
                    7: (6, 4, 4, 4, 3, 3, 3, 3),
                    8: (6, 5, 5, 3, 3, 3, 3, 1),
                    9: (6, 5, 5, 3, 3, 3, 2, 2),
                }
                chosed_tuple = atribute_pool[random.randint(1, len(atribute_pool))]

            case 300:  # 220 BP
                atribute_pool = {
                    10: (5, 5, 4, 4, 4, 3, 2, 1),
                    11: (5, 5, 4, 4, 3, 3, 3, 1),
                    12: (5, 5, 4, 4, 3, 3, 2, 2),
                    13: (5, 5, 4, 3, 3, 3, 3, 2),
                    14: (5, 4, 4, 4, 3, 3, 3, 2),
                    15: (5, 4, 4, 3, 3, 3, 3, 3),
                    16: (4, 4, 4, 4, 3, 3, 3, 3),
                    17: (4, 4, 4, 4, 3, 3, 3, 1),
                    18: (4, 4, 4, 4, 4, 4, 2, 2),
                    19: (4, 4, 4, 4, 4, 3, 3, 2),
                }
                chosed_tuple = atribute_pool[random.randint(1, len(atribute_pool))]

            case 330:  # 250 BP
                atribute_pool = {
                    1: (6, 6, 5, 5, 4, 2, 1, 1),
                    2: (6, 6, 5, 4, 4, 2, 2, 1),
                    3: (6, 6, 5, 4, 3, 3, 2, 1),
                    4: (6, 6, 5, 3, 3, 3, 3, 1),
                    5: (6, 6, 5, 3, 3, 3, 2, 2),
                    6: (6, 6, 4, 3, 3, 3, 3, 2),
                    7: (6, 5, 5, 4, 4, 3, 3, 1),
                    8: (6, 5, 5, 4, 4, 3, 2, 2),
                    9: (6, 5, 5, 4, 3, 3, 3, 2),
                    10: (6, 5, 4, 4, 4, 3, 3, 2),
                    11: (6, 4, 4, 4, 4, 3, 3, 3),
                    12: (5, 5, 5, 4, 4, 4, 3, 3),
                    13: (5, 5, 4, 4, 4, 4, 4, 3),
                    14: (5, 4, 4, 4, 4, 4, 4, 4)
                }
                chosed_tuple = atribute_pool[random.randint(1, len(atribute_pool))]

            case 380: # 300 BP   
                atribute_pool = {
                    1: (6, 6, 5, 5, 4, 4, 4, 1),
                    2: (6, 6, 5, 5, 4, 4, 3, 2),
                    3: (6, 6, 5, 5, 4, 3, 3, 3),
                    4: (6, 6, 5, 4, 4, 4, 3, 3),
                    5: (6, 6, 4, 4, 4, 4, 4, 3),
                    6: (6, 5, 5, 5, 4, 4, 4, 3),
                    7: (6, 5, 5, 4, 4, 4, 4, 4),
                    8: (5, 5, 5, 5, 5, 5, 4, 4)
                }
                chosed_tuple = atribute_pool[random.randint(1, len(atribute_pool))]

            case 400: # 320 BP
                atribute_pool = (
                    (5, 5, 5, 5, 5, 5, 5, 5),    # 8×50+0 (6) = 400
                    (6, 6, 5, 5, 5, 4, 3, 3),    # 5×50+40+2×30+50 (6) = 400
                    (6, 6, 5, 4, 4, 4, 4, 4),    # 5×40+3×50+50 (6) = 400
                    (6, 6, 5, 4, 4, 4, 4, 4),    # 3×50+5×40+50 (6) = 400
                )
                chosed_tuple = atribute_pool[random.randint(1, len(atribute_pool))]

            case 425: # 345 BP
                atribute_pool = (
                    (6, 5, 5, 5, 5, 5, 5, 5),    # 8×50+25 (6) = 425
                    (6, 6, 6, 5, 5, 4, 3, 3),    # 5×50+40+2×30+75 (6) = 425
                    (6, 6, 6, 4, 4, 4, 4, 4),    # 5×40+3×50+75 (6) = 425
                )
                chosed_tuple = atribute_pool[random.randint(1, len(atribute_pool))]


            # 330 and 380 BP don't have combination with 4 numbers
            # 425 BP up to the 600 BP is only number of 5 in pool of 6, 600 is maximum when all 6 is set
        chosen_tuple = chosed_tuple
        atributes=make_decision(chosen_tuple, pointspool)
        return atributes

def make_decision(chosed_tuple, pointspool) -> dict:
    # choose_destiny - urci zda je mag, technomancer, remeslnik, vagus... 
    choose_destiny: int = random.randint(1, 100)
    metahuman_race_decision = 100 # random.randint(96, 100)
    celk_atributy: dict = HUMAN_RACE_DICT
    RACE_DICT: dict = HUMAN_RACE_DICT
    final_atributes: dict = HUMAN_RACE_DICT
    match metahuman_race_decision:
        case metahuman_race_decision if metahuman_race_decision in range(95, 101):
            # this is Troll
            metahuman_race_decision = metahuman_race_list[4]
            RACE_DICT: dict = TROLL_RACE_DICT

        case metahuman_race_decision if metahuman_race_decision in range(90, 94):
            # this is Elf
            metahuman_race_decision = metahuman_race_list[3]
            RACE_DICT: dict = ELF_RACE_DICT

        case metahuman_race_decision if metahuman_race_decision in range(85, 89):
            # this is Dwarf
            metahuman_race_decision = metahuman_race_list[2]
            RACE_DICT: dict = DWARF_RACE_DICT

        case metahuman_race_decision if metahuman_race_decision in range(80, 84):
            # this is Orc
            metahuman_race_decision = metahuman_race_list[1]            
            RACE_DICT: dict = ORC_RACE_DICT

        case metahuman_race_decision if metahuman_race_decision in range(0, 79):
            # this is Human
            metahuman_race_decision = metahuman_race_list[0]
            RACE_DICT: dict = HUMAN_RACE_DICT
    
    # choose_destiny - urci zda je mag, technomancer, remeslnik, vagus... 
    choose_destiny: int = random.randint(1, 100)
    if choose_destiny in range(95, 100):
        atributgen = random.randint(1, 4)
        final_atributes['Magic'] = atributgen
        pointspool_skills = (pointspool + 10) - (atributgen * 10)
    elif choose_destiny in range(80, 94):
        atributgen = random.randint(1, 3)
        final_atributes['Magic'] = atributgen
        pointspool_skills = (pointspool + 10) - (atributgen * 10)
    elif choose_destiny in range(75, 79):
        atributgen = random.randint(1, 3)
        final_atributes['Resonance'] = atributgen
        pointspool_skills = (pointspool + 10) - (atributgen * 10)
    if choose_destiny in range(0, 76):
        None


    for char in LISTATR:
        addon = random.choice(chosed_tuple)
        celk_atributy[char] = [(RACE_DICT[char][3] + addon), \
                ' min: ', RACE_DICT[char][0], \
                    ' max: ', RACE_DICT[char][1], \
                        ' over: ', RACE_DICT[char][2], \
                            ' race modifier ', RACE_DICT[char][3]]
        final_atributes = celk_atributy

    final_atributes=OrderedDict(sorted(celk_atributy.items(), key=lambda t: t[0]))
    RACE_DICT=OrderedDict(sorted(RACE_DICT.items(), key=lambda t: t[0]))

    final_atributes['Metatype'] = RACE_DICT['Metatype']
    final_atributes['Edge'] = RACE_DICT['Edge'][0]

    final_atributes['Initiative'] = round((celk_atributy['Reaction'][0] + celk_atributy['Intuition'][0])/2)
    final_atributes['Initiative_Phases'] = RACE_DICT['Initiative_Phases']

    # TODO: for the future whe i will make skills
    final_atributes['BS']=RACE_DICT['BS']
    return final_atributes