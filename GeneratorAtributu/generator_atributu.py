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

# základní list s atributy, ze kterého se vybírá
listatr = ['Body', 'Agility', 'Reaction', 'Strength', 'Charisma', 'Intuition', 'Logic', 'Willpower']
usedatr = listatr
listatr = list(listatr)
race_dict: dict = {}

vysl_atr = []
# TODO: dopsat popisky - domyslet remeslniky a pod. 
# choose_destiny = None   # 96 - 100 is full Thaumaturgic, 91-95 is full shamanic, 86-90 is Thaumaturgy Adept, 81-85 is Shamanic Adept, 75-80 is Technomancer  
# is_mage = None          # 10 is full Thaumaturgic, 9 is full shamanic, 8 is Thaumaturgy Adept, 7 is Shamanic Adept, 6 physical Adept, 7 is Technomancer 

human_race_dict = {
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

orc_race_dict = {
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

dwarf_race_dict = {
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

elf_race_dict = {
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

troll_race_dict = {
    'BS': 40,
    'Metatype': "Troll",
    'Body':         (5, 10, 15, 4),
    'Agility':      (1, 5, 7, -1),
    'Reaction':     (1, 6, 9, 0),
    'Strength':     (5, 10, 15, 4),
    'Charisma':     (1, 4, 6, -2),
    'Intuition':    (1, 5, 7, -1),
    'Logic':        (1, 5, 7, -1),
    'Willpower':    (1, 6, 9, 0),
    'Initiative':   (2, 11, 16),
    'Edge':         (1, 6, 9, 1),
    'Initiative_Phases': 1,
    'Metatype Ability': "Thermographic Vision, +1 Reach, +1 natural armor (cumulative with worn armor)"
}

# this one is prepared for the future
metahuman_race_list = ['Human', 'Orc', 'Dwarf', 'Elf', 'Troll']
celk_atributy = {}

def make_atributes_loop():

    # atributgen promenna pro vygenerovanou hodnotu atributu
    atributgen: int
    # pointspool celkovy pocet bodu na postavu
    pointspool: int
    # pointspool_skills pocet bodu na skilly, Edge, rasu, Merits and Flows (neg: critters)
    pointspool_skills: int  # na platbu za edge, rasu a skilly
    # pointspool_atr_start kolik je do zacatku max na atributy - zde rozdeluji vsechny body ktere lze zakoupit (muze
    pointspool_atr_start: int  # na vypocet atributu vcetne bonusu rasy
    # pointspool/2 must be [100,150,200,250,300] and between 425 and 600 BP
    pointspool = 600
    pointspool_atr_start = int((pointspool/2) + (len(usedatr) * 10))
    pointspool_skills = pointspool_atr_start
    if pointspool_atr_start == 180:  # 100BP
        chosensystem_dict_four = {
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
        choosen_set = chosensystem_dict_four[random.randint(1, len(chosensystem_dict_four))]
        make_decision(choosen_set, pointspool)

    if pointspool_atr_start == 230:  # 150BP
        chosensystem_dict_six = {
            1: (6, 3, 3, 2, 2, 2, 2, 1),
            2: (6, 3, 2, 2, 2, 2, 2, 2),
        }
        chosensystem_dict_five = {
            1: (5, 5, 4, 3, 3, 2, 1, 1),
            2: (5, 4, 4, 3, 3, 2, 1, 1),
            3: (5, 4, 4, 3, 2, 2, 2, 1),
            4: (5, 4, 4, 2, 2, 2, 2, 2),
            5: (5, 4, 3, 3, 3, 3, 1, 1),
            6: (5, 4, 3, 3, 3, 2, 2, 1),
            7: (5, 4, 3, 3, 2, 2, 2, 2),
            8: (5, 3, 3, 3, 3, 3, 2, 1),
            9: (5, 3, 3, 3, 3, 2, 2, 2),
        }
        chosensystem_dict_four = {
            1: (4, 4, 4, 3, 3, 3, 1, 1),
            2: (4, 4, 4, 3, 3, 2, 2, 1),
            3: (4, 4, 4, 3, 2, 2, 2, 2),
            4: (4, 4, 3, 3, 3, 3, 2, 1),
            5: (4, 4, 3, 3, 3, 2, 2, 2),
            6: (4, 3, 3, 3, 3, 3, 3, 1),
            5: (4, 3, 3, 3, 3, 3, 2, 2),
            5: (3, 3, 3, 3, 3, 3, 3, 2),
        }
        choose_dict = random.randint(1, 3)
        if choose_dict == 1:
            choosen_set = chosensystem_dict_six[random.randint(1, len(chosensystem_dict_six))]
        if choose_dict == 2:
            choosen_set = chosensystem_dict_five[random.randint(1, len(chosensystem_dict_five))]
        if choose_dict == 3:
            choosen_set = chosensystem_dict_four[random.randint(1, len(chosensystem_dict_four))]
        make_decision(choosen_set, pointspool)

    if pointspool_atr_start == 280:  # 200 BP
        chosensystem_dict_six = {
            1: (6, 5, 4, 3, 3, 3, 1, 1),
            2: (6, 5, 4, 3, 2, 2, 2, 2),
            3: (6, 5, 4, 4, 3, 2, 1, 1),
            4: (6, 5, 4, 3, 3, 3, 1, 1),
            5: (6, 5, 4, 3, 2, 2, 2, 2),
            6: (6, 5, 3, 3, 3, 3, 2, 1),
            7: (6, 4, 4, 3, 3, 3, 2, 1),
            8: (6, 4, 3, 3, 3, 3, 3, 1),
            9: (6, 3, 3, 3, 3, 3, 3, 2)
        }
        chosensystem_dict_five = {
            1: (5, 5, 4, 4, 4, 3, 2, 1),
            2: (5, 5, 4, 4, 3, 3, 3, 1),
            3: (5, 5, 4, 4, 3, 3, 2, 2),
            4: (5, 5, 4, 3, 3, 3, 3, 2),
            5: (5, 4, 4, 4, 3, 3, 3, 2),
            6: (5, 4, 4, 3, 3, 3, 3, 3)
        }
        chosensystem_dict_four = {
            1: (4, 4, 4, 4, 3, 3, 3, 3),
            2: (4, 4, 4, 4, 3, 3, 3, 1),
            3: (4, 4, 4, 4, 4, 4, 2, 2),
            4: (4, 4, 4, 4, 4, 3, 3, 2),
        }
        choose_dict = random.randint(1, 3)
        if choose_dict == 1:
            choosen_set = chosensystem_dict_six[random.randint(1, len(chosensystem_dict_six))]
        if choose_dict == 2:
            choosen_set = chosensystem_dict_five[random.randint(1, len(chosensystem_dict_five))]
        if choose_dict == 3:
            choosen_set = chosensystem_dict_four[random.randint(1, len(chosensystem_dict_four))]
        make_decision(choosen_set, pointspool)

    if pointspool_atr_start == 330:  # 250 BP
        chosensystem_dict_six = {
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
            11: (6, 4, 4, 4, 4, 3, 3, 3)
        }
        chosensystem_dict_five = {
            1: (5, 5, 5, 4, 4, 4, 3, 3),
            2: (5, 5, 4, 4, 4, 4, 4, 3),
            3: (5, 4, 4, 4, 4, 4, 4, 4)
        }

        choose_dict = random.randint(1, 2)
        if choose_dict == 1:
            choosen_set = chosensystem_dict_six[random.randint(1, len(chosensystem_dict_six))]
        if choose_dict == 2:
            choosen_set = chosensystem_dict_five[random.randint(1, len(chosensystem_dict_five))]
        make_decision(choosen_set, pointspool)

    if pointspool_atr_start == 380:  # 300 BP
        chosensystem_dict_six = {
            1: (6, 6, 5, 5, 4, 4, 4, 1),
            2: (6, 6, 5, 5, 4, 4, 3, 2),
            3: (6, 6, 5, 5, 4, 3, 3, 3),
            4: (6, 6, 5, 4, 4, 4, 3, 3),
            5: (6, 6, 4, 4, 4, 4, 4, 3),
            6: (6, 5, 5, 5, 4, 4, 4, 3),
            7: (6, 5, 5, 4, 4, 4, 4, 4)
        }
        chosensystem_dict_five = {
            1: (5, 5, 5, 5, 5, 5, 4, 4)
        }
        choose_dict = random.randint(1, 2)
        if choose_dict == 1:
            choosen_set = chosensystem_dict_six[random.randint(1, len(chosensystem_dict_six))]
        if choose_dict == 2:
            choosen_set = chosensystem_dict_five[random.randint(1, len(chosensystem_dict_five))]
        make_decision(choosen_set, pointspool)

    if pointspool_atr_start >= 425 and pointspool_atr_start <= 600:
        chosen_realy_big_pool = {
            1: (6, 5, 5, 5, 5, 5, 5, 5),
            2: (6, 6, 5, 5, 5, 5, 5, 5),
            3: (6, 6, 6, 5, 5, 5, 5, 5),
            4: (6, 6, 6, 6, 5, 5, 5, 5),
            5: (6, 6, 6, 6, 6, 5, 5, 5),
            6: (6, 6, 6, 6, 6, 6, 5, 5),
            7: (6, 6, 6, 6, 6, 6, 6, 5),
            8: (6, 6, 6, 6, 6, 6, 6, 6)
        }
        choosen_set = chosen_realy_big_pool[random.randint(1, len(chosen_realy_big_pool))]
        # 330 and 380 BP don't have combination with 4 numbers
        # 425 BP up to the 600 BP is only number of 5 in pool of 6, 600 is maximum when all 6 is set
        make_decision(choosen_set, pointspool)




@dataclass
class Set_all_atributes(object):
    """ sets the non-main atributes
    """
    def __init__(self, race_dict: dict, metahuman_race: str, listatr: list, pointspool: int, choosen_set: dict):
        self.race_dict = race_dict
        self.metahuman_race = metahuman_race
        self.listatr = listatr
        self.pointspool = pointspool
        self.choosen_set = choosen_set
      
        for char in listatr:
            addon = random.choice(choosen_set)
            celk_atributy [char] = [race_dict[char][0] + addon, \
                    ' min: ', race_dict[char][0], \
                        ' max: ', race_dict[char][1], \
                            'over: ', race_dict[char][2]]

            celk_atributy[char] = race_dict[char][1] + addon

        celk_atributy['Metatype'] = race_dict['Metatype']
        celk_atributy['Edge'] = race_dict['Edge'][0]
        celk_atributy['Initiative'] = round((celk_atributy['Reaction'] + celk_atributy['Intuition'])/2)
        celk_atributy['Initiative_Phases'] = race_dict['Initiative_Phases']
        print(celk_atributy)

def make_decision(choosen_set, pointspool):
    # choose_destiny - urci zda je mag, technomancer, remeslnik, vagus... 
    choose_destiny: int = random.randint(1, 100)
    metahuman_race_decision = 100 # random.randint(96, 100)
    match metahuman_race_decision:
        case metahuman_race_decision if metahuman_race_decision in range(95, 101):
            # this is Troll
            metahuman_race_decision = metahuman_race_list[4]
            race_dict: dict = troll_race_dict

        case metahuman_race_decision if metahuman_race_decision in range(90, 96):
            # this is Elf
            metahuman_race_decision = metahuman_race_list[3]
            race_dict: dict = elf_race_dict

        case metahuman_race_decision if metahuman_race_decision in range(85, 91):
            # this is Dwarf
            metahuman_race_decision = metahuman_race_list[2]
            race_dict: dict = dwarf_race_dict

        case metahuman_race_decision if metahuman_race_decision in range(80, 86):
            # this is Orc
            metahuman_race_decision = metahuman_race_list[1]            
            race_dict: dict = orc_race_dict

        case metahuman_race_decision if metahuman_race_decision in range(0, 81):
            # this is Human
            metahuman_race_decision = metahuman_race_list[0]
            race_dict: dict = human_race_dict


    # choose_destiny - urci zda je mag, technomancer, remeslnik, vagus... 
    choose_destiny: int = random.randint(1, 100)
    if choose_destiny in range(95, 101):
        atributgen = random.randint(1, 4)
        celk_atributy['Magic'] = atributgen
        pointspool_skills = (pointspool + 10) - (atributgen * 10)
    elif choose_destiny in range(80, 96):
        atributgen = random.randint(1, 3)
        celk_atributy['Magic'] = atributgen
        pointspool_skills = (pointspool + 10) - (atributgen * 10)
    elif choose_destiny in range(75, 81):
        atributgen = random.randint(1, 3)
        celk_atributy['Resonance'] = atributgen
        pointspool_skills = (pointspool + 10) - (atributgen * 10)
    if choose_destiny in range(0, 76):
        None

    Set_all_atributes(race_dict, metahuman_race_decision, listatr, pointspool, choosen_set)
