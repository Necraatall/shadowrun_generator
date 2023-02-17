"""
    High level: kod dokaze vygenerovat atributy, ovlivnit rasou, zapsat do slovniku (vcetne Magie a resonance) a vypsat je
    Deep level: kod vyrandomuje zda dotycny je magic/resonance user (a odecte je ze zbyvajicich Pointspool)
                kod vybere z ktereho listu hodnot bude pridelovat hodnoty do atributu
                kod vybere hodnoty a priradi
                kod vybere rasu a modifikuje hodnoty atributu o jeji minima a maxima
                kod vypise hodnoty do terminalu a ulozi je docasne do slovniku TODO: jiny zpusob ukladani
    Deepest level:  kod potrebuje mit hodnotu pointspool - je to pocet bodu na celou postavu
                    kod si zjisti hodnotu poctu bodu pro generovani atributu - pointspool_atr_start (polovina pointspool) a pripocte k ni 80 (za kazdy atribut 10)
                    kod prida hodnotu 5 ke skill bodum, paklize zustal zbytek diky lichemu poctu cisel 6
                    kod si randomizuje zda je magic user, pokud ano, tak vygeneruje mu hodnotu k atributu Magic/Reason, zapise jej do dict a listu
                    kod zjisti si kolik bodu ma na skilly a vygeneruje si jeden list z ktereho bude plnit random nepouzity atribut (100, 200, 250, 300, 425 a vice do hodnoty 600)
                    kod si zavola meta cast - rasy, a upravi hodnoty v dict i v listech
                    kod vypise vysledek

"""
import random
from typing import Dict
from collections import OrderedDict


# základní list s atributy, ze kterého se vybírá
LISTATR = ['Body', 'Agility', 'Reaction', 'Strength', 'Charisma', 'Intuition', 'Logic', 'Willpower']
usedatr = LISTATR
LISTATR = list(LISTATR)
RACE_DICT: dict = {}
final_atributes: dict= {}
chosed_tuple: tuple = ()
# adventages celkovy pocet bodu na obdareni a postizeni
adventages: int = 0


HUMAN_RACE_DICT = {
    'BS':                   0,
    'Metatype':             "Human",
    'Body':                 (1, 6, 9, 0),
    'Agility':              (1, 6, 9, 0),
    'Reaction':             (1, 6, 9, 0),
    'Strength':             (1, 6, 9, 0),
    'Charisma':             (1, 6, 9, 0),
    'Intuition':            (1, 6, 9, 0),
    'Logic':                (1, 6, 9, 0),
    'Willpower':            (1, 6, 9, 0),
    'Initiative':           (2, 12, 18),
    'Edge':                 (2, 7, 10, 1),
    'Initiative_Phases':    1,
    'Metatype Ability':     "+1 Edge"
}

ORC_RACE_DICT = {
    'BS':                   20,
    'Metatype':             "Orc",
    'Body':                 (4, 9, 13, 3),
    'Agility':              (1, 6, 9, 0),
    'Reaction':             (1, 6, 9, 0),
    'Strength':             (3, 8, 12, 2),
    'Charisma':             (1, 5, 7, -1),
    'Intuition':            (1, 6, 9, 0),
    'Logic':                (1, 5, 7, -1),
    'Willpower':            (1, 6, 9, 0),
    'Initiative':           (2, 12, 18),
    'Edge':                 (1, 6, 9, 0),
    'Initiative_Phases':    1,
    'Metatype Ability':     "Low-Light Vision"
}

DWARF_RACE_DICT = {
    'BS':                   25,
    'Metatype':             "Dwarf",
    'Body':                 (2, 7, 10, 1),
    'Agility':              (1, 6, 9, 0),
    'Reaction':             (1, 5, 7, -1),
    'Strength':             (3, 8, 12, 2),
    'Charisma':             (1, 6, 9, 0),
    'Intuition':            (1, 6, 9, 0),
    'Logic':                (1, 6, 9, 0),
    'Willpower':            (2, 7, 10, 0),
    'Initiative':           (2, 11, 16),
    'Edge':                 (1, 6, 9, 0),
    'Initiative_Phases':    1,
    'Metatype Ability':     "Thermographic Vision, +2 dice for Body Tests to resist pathogens and toxins"
}

ELF_RACE_DICT = {
    'BS':                   30,
    'Metatype':             "Elf",
    'Body':                 (1, 6, 9, 0),
    'Agility':              (2, 7, 10, 1),
    'Reaction':             (1, 6, 9, 0),
    'Strength':             (1, 6, 9, 0),
    'Charisma':             (3, 8, 12, 2),
    'Intuition':            (1, 6, 9, 0),
    'Logic':                (1, 6, 9, 0),
    'Willpower':            (1, 6, 9, 0),
    'Initiative':           (2, 12, 18),
    'Edge':                 (1, 6, 9, 0),
    'Initiative_Phases':    1,
    'Metatype Ability':     "Low-Light Vision"
}

TROLL_RACE_DICT = {
    'BS':                   40,
    'Metatype':             "Troll",
    'Body':                 (5, 10, 15, 4),
    'Agility':              (1, 5, 7, -1),
    'Reaction':             (1, 6, 9, 0),
    'Strength':             (5, 10, 15, 4),
    'Charisma':             (1, 4, 6, -2),
    'Intuition':            (1, 5, 7, -1),
    'Logic':                (1, 5, 7, -1),
    'Willpower':            (1, 6, 9, 0),
    'Initiative':           (2, 11, 16),
    'Edge':                 (1, 6, 9, 1),
    'Initiative_Phases':    1,
    'Metatype Ability':     "Thermographic Vision, +1 Reach, +1 natural armor (cumulative with worn armor)"
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
        # pointspool/2 must be [200, 300, 340, 390, 400, 430, 440, 500, 600, 640, 690]
        pointspool = random.choice((200, 300, 340, 390, 400, 430, 440, 500, 600, 640, 690))
        # TODO: better way for counting atributes and so one but there is realy huge pool of skils
        pointspool_atr_start = round((pointspool/2) + (len(usedatr) * 10))
        pointspool_skills = pointspool - pointspool_atr_start + adventages
        match pointspool_atr_start:
            case 180:  # 100BP
                atribute_pool = (
                    (4, 4, 2, 2, 2, 2, 1, 1),
                    (4, 3, 3, 3, 2, 1, 1, 1),
                    (4, 3, 3, 2, 2, 2, 1, 1),
                    (4, 3, 2, 2, 2, 2, 2, 1),
                    (4, 2, 2, 2, 2, 2, 2, 2),
                    (3, 3, 3, 3, 3, 1, 1, 1),
                    (3, 3, 3, 3, 2, 2, 1, 1),
                    (3, 3, 3, 2, 2, 2, 2, 1),
                    (3, 3, 2, 2, 2, 2, 2, 2),
                )
                chosed_tuple = atribute_pool[random.randint(0, len(atribute_pool)-1)]

            case 230:  # 150BP
                atribute_pool = (
                    (5, 5, 4, 3, 3, 2, 1, 1),
                    (5, 4, 4, 3, 3, 2, 1, 1),
                    (5, 4, 4, 3, 2, 2, 2, 1),
                    (5, 4, 4, 2, 2, 2, 2, 2),
                    (5, 4, 3, 3, 3, 3, 1, 1),
                    (5, 4, 3, 3, 3, 2, 2, 1),
                    (5, 4, 3, 3, 2, 2, 2, 2),
                    (5, 3, 3, 3, 3, 3, 2, 1),
                    (5, 3, 3, 3, 3, 2, 2, 2),
                    (4, 4, 4, 3, 3, 3, 1, 1),
                    (4, 4, 4, 3, 3, 2, 2, 1),
                    (4, 4, 4, 3, 2, 2, 2, 2),
                    (4, 4, 3, 3, 3, 3, 2, 1),
                    (4, 4, 3, 3, 3, 2, 2, 2),
                    (4, 3, 3, 3, 3, 3, 3, 1),
                    (4, 3, 3, 3, 3, 3, 2, 2),
                    (3, 3, 3, 3, 3, 3, 3, 2),
                )
                chosed_tuple = atribute_pool[random.randint(0, len(atribute_pool)-1)]
            case 250:  # 170BP
                atribute_pool = (
                    (5, 5, 3, 3, 3, 2, 2, 2),
                    (5, 4, 4, 3, 3, 2, 2, 2),
                    (5, 4, 4, 3, 3, 3, 2, 1),
                    (5, 4, 4, 3, 3, 2, 2, 2),
                    (5, 4, 3, 3, 3, 3, 2, 2),
                    (5, 5, 4, 4, 2, 2, 2, 1),
                    (5, 5, 5, 2, 2, 2, 2, 2),
                    (5, 3, 3, 3, 3, 3, 3, 2),
                    (4, 4, 4, 3, 3, 3, 2, 2),
                    (4, 4, 3, 3, 3, 3, 3, 2),
                    (4, 3, 3, 3, 3, 3, 3, 3),
                )
                chosed_tuple = atribute_pool[random.randint(0, len(atribute_pool)-1)]
            case 275:  # 195 BP
                atribute_pool = (
                    (6, 5, 4, 3, 3, 3, 1, 1),
                    (6, 5, 4, 3, 2, 2, 2, 2),
                    (6, 5, 4, 4, 3, 2, 1, 1),
                    (6, 5, 4, 3, 3, 3, 1, 1),
                    (6, 5, 4, 3, 2, 2, 2, 2),
                    (6, 5, 3, 3, 3, 3, 2, 1),
                    (6, 4, 4, 3, 3, 3, 2, 1),
                    (6, 4, 3, 3, 3, 3, 3, 1),
                    (6, 3, 3, 3, 3, 3, 3, 2),
                    )
                chosed_tuple = atribute_pool[random.randint(0, len(atribute_pool)-1)]
            case 280:  # 200 BP
                atribute_pool = (
                    (5, 5, 4, 4, 4, 3, 2, 1),
                    (5, 5, 4, 4, 3, 3, 3, 1),
                    (5, 5, 4, 4, 3, 3, 2, 2),
                    (5, 5, 4, 3, 3, 3, 3, 2),
                    (5, 4, 4, 4, 3, 3, 3, 2),
                    (5, 4, 4, 3, 3, 3, 3, 3),
                    (4, 4, 4, 4, 3, 3, 3, 3),
                    (4, 4, 4, 4, 4, 4, 2, 2),
                    (4, 4, 4, 4, 4, 3, 3, 2),
                )
                chosed_tuple = atribute_pool[random.randint(0, len(atribute_pool)-1)]

            case 295:  # 215 BP
                atribute_pool = (
                    (6, 5, 4, 4, 4, 3, 2, 1),
                    (6, 5, 4, 4, 3, 3, 3, 1),
                    (6, 5, 4, 4, 3, 3, 2, 2),
                    (6, 5, 4, 3, 3, 3, 3, 2),
                    (6, 4, 4, 4, 3, 3, 3, 2),
                    (6, 4, 4, 3, 3, 3, 3, 3),
                    (6, 4, 4, 4, 3, 3, 3, 3),
                    (6, 5, 5, 3, 3, 3, 3, 1),
                    (6, 5, 5, 3, 3, 3, 2, 2),
                )
                chosed_tuple = atribute_pool[random.randint(0, len(atribute_pool)-1)]

            case 300:  # 220 BP
                atribute_pool = (
                    (5, 5, 4, 4, 4, 3, 2, 1),
                    (5, 5, 4, 4, 3, 3, 3, 1),
                    (5, 5, 4, 4, 3, 3, 2, 2),
                    (5, 5, 4, 3, 3, 3, 3, 2),
                    (5, 4, 4, 4, 3, 3, 3, 2),
                    (5, 4, 4, 3, 3, 3, 3, 3),
                    (4, 4, 4, 4, 3, 3, 3, 3),
                    (4, 4, 4, 4, 3, 3, 3, 1),
                    (4, 4, 4, 4, 4, 4, 2, 2),
                    (4, 4, 4, 4, 4, 3, 3, 2),
                )
                chosed_tuple = atribute_pool[random.randint(0, len(atribute_pool)-1)]

            case 330:  # 250 BP
                atribute_pool = (
                    (6, 6, 5, 5, 4, 2, 1, 1),
                    (6, 6, 5, 4, 4, 2, 2, 1),
                    (6, 6, 5, 4, 3, 3, 2, 1),
                    (6, 6, 5, 3, 3, 3, 3, 1),
                    (6, 6, 5, 3, 3, 3, 2, 2),
                    (6, 6, 4, 3, 3, 3, 3, 2),
                    (6, 5, 5, 4, 4, 3, 3, 1),
                    (6, 5, 5, 4, 4, 3, 2, 2),
                    (6, 5, 5, 4, 3, 3, 3, 2),
                    (6, 5, 4, 4, 4, 3, 3, 2),
                    (6, 4, 4, 4, 4, 3, 3, 3),
                    (5, 5, 5, 4, 4, 4, 3, 3),
                    (5, 5, 4, 4, 4, 4, 4, 3),
                    (5, 4, 4, 4, 4, 4, 4, 4)
                )
                chosed_tuple = atribute_pool[random.randint(0, len(atribute_pool)-1)]

            case 380: # 300 BP   
                atribute_pool = (
                    (6, 6, 5, 5, 4, 4, 4, 1),
                    (6, 6, 5, 5, 4, 4, 3, 2),
                    (6, 6, 5, 5, 4, 3, 3, 3),
                    (6, 6, 5, 4, 4, 4, 3, 3),
                    (6, 6, 4, 4, 4, 4, 4, 3),
                    (6, 5, 5, 5, 4, 4, 4, 3),
                    (6, 5, 5, 4, 4, 4, 4, 4),
                    (5, 5, 5, 5, 5, 5, 4, 4)
                )
                chosed_tuple = atribute_pool[random.randint(0, len(atribute_pool)-1)]

            case 400: # 320 BP
                atribute_pool = (
                    (5, 5, 5, 5, 5, 5, 5, 5),
                    (6, 6, 5, 5, 5, 4, 3, 3),
                    (6, 6, 5, 4, 4, 4, 4, 4),
                    (6, 6, 5, 4, 4, 4, 4, 4),
                )
                chosed_tuple = atribute_pool[random.randint(0, len(atribute_pool)-1)]

            case 425: # 345 BP
                atribute_pool = (
                    (6, 5, 5, 5, 5, 5, 5, 5),
                    (6, 6, 6, 5, 5, 4, 3, 3),
                    (6, 6, 6, 4, 4, 4, 4, 4),
                )
                chosed_tuple = atribute_pool[random.randint(0, len(atribute_pool)-1)]

        chosen_tuple = chosed_tuple

        atributes=make_decision(chosen_tuple, pointspool, pointspool_skills)
        pointspool_skills = atributes[1]
        return atributes[0]

def make_decision(chosed_tuple:dict, pointspool:int, pointspool_skills:int) -> dict:
    # choose_destiny - urci zda je mag, technomancer, remeslnik, vagus... 
    choose_destiny: int = random.randint(1, 100)
    metahuman_race_decision = random.randint(0, 100)
    print ("\n \nmetahuman_race_decision", metahuman_race_decision, "\n")
    celk_atributy: dict = HUMAN_RACE_DICT
    RACE_DICT: dict = HUMAN_RACE_DICT
    final_atributes: dict = HUMAN_RACE_DICT
    match metahuman_race_decision:
        case metahuman_race_decision if metahuman_race_decision in range(95, 101):
            # this is Troll
            metahuman_race_decision = metahuman_race_list[4]
            RACE_DICT: dict = TROLL_RACE_DICT

        case metahuman_race_decision if metahuman_race_decision in range(90, 95):
            # this is Elf
            metahuman_race_decision = metahuman_race_list[3]
            RACE_DICT: dict = ELF_RACE_DICT

        case metahuman_race_decision if metahuman_race_decision in range(85, 90):
            # this is Dwarf
            metahuman_race_decision = metahuman_race_list[2]
            RACE_DICT: dict = DWARF_RACE_DICT

        case metahuman_race_decision if metahuman_race_decision in range(80, 85):
            # this is Orc
            metahuman_race_decision = metahuman_race_list[1]            
            RACE_DICT: dict = ORC_RACE_DICT

        case metahuman_race_decision if metahuman_race_decision in range(0, 80):
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
                'min:', RACE_DICT[char][0], \
                    'max:', RACE_DICT[char][1], \
                        'over:', RACE_DICT[char][2], \
                            'race modifier', RACE_DICT[char][3]]
        final_atributes = celk_atributy

    final_atributes=OrderedDict(sorted(celk_atributy.items(), key=lambda t: t[0]))
    RACE_DICT=OrderedDict(sorted(RACE_DICT.items(), key=lambda t: t[0]))

    atributgen = random.randint(1, 6)
    if final_atributes['Metatype']=="Human":
        atributgen = random.randint(2, 7)
        final_atributes['Edge'] = atributgen
    else: final_atributes['Edge'] = atributgen
    final_atributes['Metatype'] = RACE_DICT['Metatype']
    final_atributes['Metatype Ability'] = RACE_DICT['Metatype Ability']

    final_atributes['Initiative'] = round((celk_atributy['Reaction'][0] + celk_atributy['Intuition'][0])/2)
    final_atributes['Initiative_Phases'] = RACE_DICT['Initiative_Phases']

    # TODO: for the future when i will make skills
    final_atributes['BS']=RACE_DICT['BS']
    return final_atributes, pointspool_skills