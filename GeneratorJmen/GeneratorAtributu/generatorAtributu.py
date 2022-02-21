'''
    High level: kod dokaze vygenerovat atributy, ovlivnit rasou, zapsat do atributes_dict (vcetne Magie a resonance) a vypsat je
    Deep level: kod vyrandomuje zda dotycny je magic/resonance user (a odecte je ze zbyvajicich Pointspool)
                kod vybere z ktereho listu hodnot bude pridelovat hodnoty do atributu
                kod vybere hodnoty a priradi
                kod vybere rasu a modifikuje hodnoty atributu o jeji minima a maxima
                kod vypise hodnoty do terminalu a ulozi je docasne do slovniku 
    Deepest level:  kod potrebuje mit hodnotu pointspool - je to pocet bodu na celou postavu
                    kod si zjisti hodnotu poctu bodu pro generovani atributu - pointspool_atr_start (polovina pointspool) a pripocte k ni 80 (za kazdy atribut 10)
                    kod si randomizuje zda je magic user, pokud ano, tak 

'''

import random
# startovní body na rozdělení, zatím fix hodnota 280 do zakl. 8mi atr.
# dodelat pro: 100, 150, 250, 300

# základní list s atributy, ze kterého se vybírá
listatr = ['Body', 'Agility', 'Reaction', 'Strenght', 'Charisma', 'Intuition', 'Logic', 'Willpower']
            
vysl_atr =[]
# TODO: dopsat popisky - domyslet remeslniky a pod. 
# choose_destiny = None   # 96 - 100 is full Thaumaturgic, 91-95 is full shamanic, 86-90 is Thaumaturgy Adept, 81-85 is Shamanic Adept, 75-80 is Technomancer  
# is_mage = None          # 10 is full Thaumaturgic, 9 is full shamanic, 8 is Thaumaturgy Adept, 7 is Shamanic Adept, 6 physical Adept, 7 is Technomancer 

atributes_dict = {
    'Metatype':           "Human",
    'Body':                     1,
    'Agility':                  1, 
    'Reaction':                 1, 
    'Strenght':                 1, 
    'Charisma':                 1, 
    'Intuition':                1, 
    'Logic':                    1,
    'Willpower':                1,
    'Iniciative':               1, 
    'Edge':                     1,
    'Iniciative_Phases':        1,
    'Metatype Ability':         ""
    }

def make_decision():
    #make_decision = random.randint(1, 100)
    choose_destiny: int = random.randint(1, 100)
    atributgen: int
    pointspool: int         
    pointspool_skills: int      # na platbu za edge, rasu a skilly
    pointspool_atr_start: int   # na vypocet atributu vcetne bonusu rasy
    # pointspool/2 must be [100,150,200,250,300] and between 425 and 600 BP
    pointspool = 500

    pointspool_atr_start = int((pointspool / 2) + (len(listatr)*10))
    max: int = len(listatr)
    print('Počáteční body na rozdělení:', (pointspool_atr_start - 80))
    match choose_destiny:
        case choose_destiny if choose_destiny in range(95, 101):
            atributgen = random.randint(1, 4)
            atributes_dict['Magic'] = atributgen
            pointspool = (pointspool + 10) - (atributgen * 10)
            max = len(listatr) + 1
        case choose_destiny if choose_destiny in range(80, 96):
            atributgen = random.randint(1, 3)
            atributes_dict['Magic'] = atributgen
            pointspool = (pointspool + 10) - (atributgen * 10)
            max = len(listatr) + 1
        case choose_destiny if choose_destiny in range(75, 81):
            atributgen = random.randint(1, 3)
            atributes_dict['Resonance'] = atributgen
            pointspool = (pointspool + 10) - (atributgen * 10)
            max = len(listatr) + 1 
        case choose_destiny if choose_destiny in range(0, 76):
            atributgen = 0
            max = len(listatr) + 1
    if choose_destiny is None:
            atributgen = 0
            max = len(listatr) + 1
    result = [atributgen, pointspool_atr_start, max]
    #print('Stav bodu:', pointspool)
    return result


def make_atributes_loop():
    i: int = 1
    decision = make_decision()
    atributgen = int(decision[0])
    pointspool_atr_start = decision[1]
    pointspool_atr = int(decision[1])
    max = int(decision[2])
    while i < max:
        if pointspool_atr_start == 180:   #100BP
            chosensystem_dict_six = {
                1 :   [6,	4,	1,	1,	1,	1,	1,	1],
                2 :   [6,	3,	2,	1,	1,	1,	1,	1],
                3 :   [6,	2,	2,	2,	1,	1,	1,	1]
            }
            chosensystem_dict_five = {
                1 :   [5,	5,	3,	1,	1,	1,	1,	1], 
                2 :   [5,	5,	2,	2,	1,	1,	1,	1], 
                3 :   [5,	4,	4,	1,	1,	1,	1,	1], 
                4 :   [5,	4,	3,	2,	1,	1,	1,	1], 
                5 :   [5,	4,	2,	2,	2,	1,	1,	1], 
                6 :   [5,	3,	3,	3,	1,	1,	1,	1],
                7 :   [5,	3,	2,	2,	2,	2,	1,	1],
                8 :   [5,	2,	2,	2,	2,	2,	2,	1]
            }
            chosensystem_dict_four = {
                1 :   [4,	4,	4,	2,	1,	1,	1,	1],
                2 :   [4,	4,	3,	3,	1,	1,	1,	1],
                3 :   [4,	4,	3,	2,	2,	1,	1,	1],
                4 :   [4,	4,	2,	2,	2,	2,	1,	1],
                5 :   [4,	3,	3,	3,	2,	1,	1,	1],
                6 :   [4,	3,	3,	2,	2,	2,	1,	1],
                7 :   [4,	3,	2,	2,	2,	2,	2,	1],
                8 :   [4,	2,	2,	2,	2,	2,	2,	2],
                9 :   [3,	3,	3,	3,	3,	1,	1,	1],                
                10 :  [3,	3,	3,	3,	2,	2,	1,	1],
                11 :  [3,	3,	3,	2,	2,	2,	2,	1],
                12 :  [3,	3,	2,	2,	2,	2,	2,	2]                                               
            }
        if pointspool_atr_start == 230:   #150BP
            chosensystem_dict_six = {
                1 :   [6,	5,	5,	1,	1,	1,	1,	1],
                2 :   [6,	5,	4,	2,	1,	1,	1,	1],
                3 :   [6,	5,	3,	3,	1,	1,	1,	1], 
                4 :   [6,	4,	3,	3,	2,	1,	1,	1],
                5 :   [6,	3,	3,	3,	3,	1,	1,	1],
                6 :   [6,	3,	3,	3,	2,	2,	1,	1],
                7 :   [6,	3,	3,	2,	2,	2,	2,	1],
                8 :   [6,	3,	2,	2,	2,	2,	2,	2]
            }
            chosensystem_dict_five = {
                1 :   [5,	5,	4,	4,	2,	1,	1,	1], 
                2 :   [5,	5,	4,	3,	3,	1,	1,	1], 
                3 :   [5,	5,	4,	3,	3,	2,	1,	1], 
                4 :   [5,	4,	4,	4,	3,	1,	1,	1], 
                5 :   [5,	4,	4,	3,	3,	2,	1,	1], 
                6 :   [5,	4,	4,	3,	2,	2,	2,	1], 
                7 :   [5,	4,	4,	2,	2,	2,	2,	2], 
                8 :   [5,	4,	3,	3,	3,	3,	1,	1], 
                9 :   [5,	4,	3,	3,	3,	2,	2,	1], 
                10 :  [5,	4,	3,	3,	2,	2,	2,	2], 
                11 :  [5,	3,	3,	3,	3,	3,	2,	1], 
                12 :  [5,	3,	3,	3,	3,	2,	2,	2]
            }
            chosensystem_dict_four = {
                1 :   [4,	4,	4,	3,	3,	3,	1,	1],
                2 :   [4,	4,	4,	3,	3,	2,	2,	1], 
                3 :   [4,	4,	4,	3,	2,	2,	2,	2], 
                4 :   [4,	4,	3,	3,	3,	3,	2,	1], 
                5 :   [4,	4,	3,	3,	3,	2,	2,	2], 
                6 :   [4,	3,	3,	3,	3,	3,	3,	1], 
                5 :   [4,	3,	3,	3,	3,	3,	2,	2], 
                5 :   [3,	3,	3,	3,	3,	3,	3,	2]
            }
        if pointspool_atr_start == 280:   #200 BP
            chosensystem_dict_six = {
                1 :   [6,	5,	4,	3,	3,	3,	1,	1],
                2 :   [6,	5,	4,	3,	2,	2,	2,	2],
                3 :   [6,	5,	4,	4,	3,	2,	1,	1],
                4 :   [6,	5,	4,	3,	3,	3,	1,	1],
                5 :   [6,	5,	4,	3,	2,	2,	2,	2],
                6 :   [6,	5,	3,	3,	3,	3,	2,	1],
                7 :   [6,	4,	4,	3,	3,	3,	2,	1],
                8 :   [6,	4,	3,	3,	3,	3,	3,	1],
                9 :   [6,	3,	3,	3,	3,	3,	3,	2]
            }
            chosensystem_dict_five = {
                1 :   [5,	5,	4,	4,	4,	3,	2,	1], 
                2 :   [5,	5,	4,	4,	3,	3,	3,	1], 
                3 :   [5,	5,	4,	4,	3,	3,	2,	2], 
                4 :   [5,	5,	4,	3,	3,	3,	3,	2], 
                5 :   [5,	4,	4,	4,	3,	3,	3,	2], 
                6 :   [5,	4,	4,	3,	3,	3,	3,	3]  
            }
            chosensystem_dict_four = {
                1 :   [4,	4,	4,	4,	3,	3,	3,	3],
                2 :   [4,	4,	4,	4,	3,	3,	3,	1],
                3 :   [4,	4,	4,	4,	4,	4,	2,	2],
                4 :   [4,	4,	4,	4,	4,	3,	3,	2],
            }
        if pointspool_atr_start == 330:   #250 BP
            chosensystem_dict_six = {
                1 :   [6,	6,	5,	5,	4,	2,	1,	1],
                2 :   [6,	6,	5,	4,	4,	2,	2,	1],
                3 :   [6,	6,	5,	4,	3,	3,	2,	1], 
                4 :   [6,	6,	5,	3,	3,	3,	3,	1],
                5 :   [6,	6,	5,	3,	3,	3,	2,	2], 
                6 :   [6,	6,	4,	3,	3,	3,	3,	2], 
                7 :   [6,	5,	5,	4,	4,	3,	3,	1], 
                8 :   [6,	5,	5,	4,	4,	3,	2,	2], 
                9 :   [6,	5,	5,	4,	3,	3,	3,	2], 
                10 :  [6,	5,	4,	4,	4,	3,	3,	2], 
                11 :  [6,	4,	4,	4,	4,	3,	3,	3]
            }
            chosensystem_dict_five = {
                1 :   [5,	5,	5,	4,	4,	4,	3,	3], 
                2 :   [5,	5,	4,	4,	4,	4,	4,	3], 
                3 :   [5,	4,	4,	4,	4,	4,	4,	4]
            }
        if pointspool_atr_start == 380:   #300 BP
            chosensystem_dict_six = {
                1 :   [6,	6,	5,	5,	4,	4,	4,	1],
                2 :   [6,	6,	5,	5,	4,	4,	3,	2],
                3 :   [6,	6,	5,	5,	4,	3,	3,	3], 
                4 :   [6,	6,	5,	4,	4,	4,	3,	3], 
                5 :   [6,	6,	4,	4,	4,	4,	4,	3], 
                6 :   [6,	5,	5,	5,	4,	4,	4,	3], 
                7 :   [6,	5,	5,	4,	4,	4,	4,	4]
            }
            chosensystem_dict_five = {
                1 :   [5,	5,	5,	5,	5,	5,	4,	4] 
            }
        if pointspool_atr_start >= 425 and pointspool_atr <= 600 :
            chosen_realy_big_pool = {
                1 :   [6,	5,	5,	5,	5,	5,	5,	5],
                2 :   [6,	6,	5,	5,	5,	5,	5,	5],
                3 :   [6,	6,	6,	5,	5,	5,	5,	5],
                4 :   [6,	6,	6,	6,	5,	5,	5,	5], 
                5 :   [6,	6,	6,	6,	6,	5,	5,	5], 
                6 :   [6,	6,	6,	6,	6,	6,	5,	5], 
                7 :   [6,	6,	6,	6,	6,	6,	6,	5], 
                8 :   [6,	6,	6,	6,	6,	6,	6,	6]
            }
        # 330 and 380 BP dont have combination with 4 numbers
        # 425 BP up to the 600 BP is only number of 5 in pool of 6, 600 is maximum when all 6 is set
        if i==1: 
            if pointspool_atr_start >= 425 and pointspool_atr_start < 600: 
                number_of_five = int((pointspool_atr_start - 80 - 400)/25)
                choosen_set = chosen_realy_big_pool[number_of_five]

            if pointspool_atr_start >= 180 and pointspool_atr_start <= 230:    
                atributgen = random.randint(4, 6)
            elif pointspool_atr_start == 330 or pointspool_atr_start == 380: 
                atributgen = random.randint(5, 6)

        if pointspool_atr_start >= 180 and pointspool_atr_start <= 230 or pointspool_atr_start == 330 or pointspool_atr_start == 380:
            match atributgen:
                case 6:
                    if i == 1:
                        choose = random.randint(1, len(chosensystem_dict_six.keys()))
                        choosen_set = chosensystem_dict_six[choose]
                case 5:
                    if i == 1:
                        choose = random.randint(1, len(chosensystem_dict_five.keys()))
                        choosen_set = chosensystem_dict_five[choose]
                case 4:        
                    if i == 1:
                        choose = random.randint(1, len(chosensystem_dict_four.keys()))
                        choosen_set = chosensystem_dict_four[choose]

        atributgen = choosen_set[i-1]
                             
        if atributgen == 6:
            pointspool_atr = (pointspool_atr - (atributgen * 10)) - 15
        else: pointspool_atr = pointspool_atr - (atributgen * 10)
        
        loop_i = i

        atribut2 = random.choice(listatr)
        listatr.remove(atribut2)
        vysl_atr.append(atribut2 + " " + str(atributgen))
        atributes_dict[atribut2] = atributgen
        
        if loop_i == max-1:
            # prints list of results
            print(vysl_atr)
            # to count Iniciative, need reaction and Intuition divided by 2 and save it to the dictionary
            pom = atributes_dict['Reaction'] + atributes_dict['Intuition']
            atributes_dict['Iniciative'] = pom
            # runs function for combining atribut values with metahuman min/max-es
            metahuman_race(atributes_dict)
            # print result
            print(atributes_dict)
        i += 1


def metahuman_race(atributes_dict):
    human_race_dict = {
    'BS':                   0,
    'Metatype':             "Human",
    'Body':                 [1, 6,  9,  0],
    'Agility':              [1, 6,  9,  0],
    'Reaction':             [1, 6,  9,  0],
    'Strenght':             [1, 6,  9,  0],
    'Charisma':             [1, 6,  9,  0], 
    'Intuition':            [1, 6,  9,  0], 
    'Logic':                [1, 6,  9,  0],
    'Willpower':            [1, 6,  9,  0],
    'Iniciative':           [2, 12, 18],
    'Edge':                 [2, 7, 10,  1],
    'Iniciative_Phases':    1,
    'Metatype Ability':     "+1 Edge"
    }
    
    orc_race_dict = {
    'BS':                   20,
    'Metatype':             "Orc",
    'Body':                 [4, 9,  13, 3],
    'Agility':              [1, 6,  9,  0],
    'Reaction':             [1, 6,  9,  0],
    'Strenght':             [3, 8,  12, 2],
    'Charisma':             [1, 5,  7, -1],
    'Intuition':            [1, 6,  9,  0],
    'Logic':                [1, 5,  7, -1],
    'Willpower':            [1, 6,  9,  0],
    'Iniciative':           [2, 12, 18],
    'Edge':                 [1, 6,  9,  0],
    'Iniciative_Phases':    1,
    'Metatype Ability':     "Low-Light Vision"
    }

    dwarf_race_dict = {
    'BS':                   25,
    'Metatype':             "Dwarf",
    'Body':                 [2, 7,  10, 1],
    'Agility':              [1, 6,  9,  0],
    'Reaction':             [1, 5,  7, -1],
    'Strenght':             [3, 8,  12, 2],
    'Charisma':             [1, 6,  9,  0], 
    'Intuition':            [1, 6,  9,  0], 
    'Logic':                [1, 6,  9,  0],
    'Willpower':            [2, 7, 10,  0],
    'Iniciative':           [2, 11, 16],
    'Edge':                 [1, 6,  9,  0],
    'Iniciative_Phases':    1,
    'Metatype Ability':     "Thermographic Vision, +2 dice for Body Tests to resist pathogens and toxins"
    }    

    elf_race_dict = {
    'BS':                   30,
    'Metatype':             "Elf",
    'Body':                 [1, 6,  9,  0],
    'Agility':              [2, 7,  10, 1],
    'Reaction':             [1, 6,  9,  0],
    'Strenght':             [1, 6,  9,  0],
    'Charisma':             [3, 8,  12, 2],
    'Intuition':            [1, 6,  9,  0],
    'Logic':                [1, 6,  9,  0],
    'Willpower':            [1, 6,  9,  0],
    'Iniciative':           [2, 12, 18],
    'Edge':                 [1, 6,  9,  0],
    'Iniciative_Phases':    1,
    'Metatype Ability':     "Low-Light Vision"
    }

    troll_race_dict = {
    'BS':                   40,
    'Metatype':             "Troll",
    'Body':                 [5, 10, 15, 4],
    'Agility':              [1, 5,  7, -1],
    'Reaction':             [1, 6,  9,  0],
    'Strenght':             [5, 10, 15, 4],
    'Charisma':             [1, 4,  6, -2], 
    'Intuition':            [1, 5,  7, -1], 
    'Logic':                [1, 5,  7, -1],
    'Willpower':            [1, 6,  9,  0],
    'Iniciative':           [2, 11, 16],
    'Edge':                 [2, 7, 10,  1],
    'Iniciative_Phases':    1,
    'Metatype Ability':     "Thermographic Vision, +1 Reach, +1 natural armor (cumulative with worn armor)"
    }

    # this one is prepared for the future
    metahuman_race_list = ['Human', 'Orc', 'Dwarf', 'Elf', 'Troll']
    celk_atributy = []

    metahuman_race_decision = random.randint(96, 100)
    match metahuman_race_decision: 
        case metahuman_race_decision if metahuman_race_decision in range(95, 101):
            # this is Troll
            m = 1
            for key, value in troll_race_dict.items():
                if key != 'BS' and key != 'Iniciative_Phases':
                    if key == 'Metatype' or key == 'Metatype Ability': 
                        atributes_dict[key] = value
                    elif key == 'Iniciative': atributes_dict[key] = atributes_dict['Reaction'] + atributes_dict['Intuition']
                    elif key == 'Iniciative_Phases': pass
                    else: 
                        atributes_dict[key] = atributes_dict[key] + troll_race_dict[key][3]
                        celk_atributy.append(str(key + " " + str(troll_race_dict[key][1]) + " min " + str(troll_race_dict[key][0]) + " max " + str(troll_race_dict[key][2])))
                        if atributes_dict.get(key) < 1:
                            atributes_dict[key] = 1
                            celk_atributy.append(str(key + " " + str(troll_race_dict[key][1]) + " min " + str(troll_race_dict[key][0]) + " max " + str(troll_race_dict[key][2])))
                if m == len(vysl_atr)+2: 
                    print(celk_atributy)            
                m += +1
        case metahuman_race_decision if metahuman_race_decision in range(90, 96):
            # this is Elf
            m = 1
            for key, value in elf_race_dict.items():  
                if key != 'BS' and key != 'Iniciative_Phases':
                    if key == 'Metatype' or key == 'Metatype Ability': 
                        atributes_dict[key] = value
                    elif key == 'Iniciative': atributes_dict[key] = atributes_dict['Reaction'] + atributes_dict['Intuition']
                    elif key == 'Iniciative_Phases': pass
                    else: 
                        atributes_dict[key] = atributes_dict[key] + elf_race_dict[key][3]
                        celk_atributy.append(str(key + " " + str(elf_race_dict[key][1]) + " min " + str(elf_race_dict[key][0]) + " max " + str(elf_race_dict[key][2])))
                        if atributes_dict.get(key) < 1:
                            atributes_dict[key] = 1
                            celk_atributy.append(str(key + " " + str(elf_race_dict[key][1]) + " min " + str(elf_race_dict[key][0]) + " max " + str(elf_race_dict[key][2])))
                if m == len(vysl_atr)+2: 
                    print(celk_atributy)                               
                m += +1
        case metahuman_race_decision if metahuman_race_decision in range(85, 91):
            # this is Dwarf
            m = 1
            for key, value in dwarf_race_dict.items(): 
                if key != 'BS' and key != 'Iniciative_Phases':
                    if key == 'Metatype' or key == 'Metatype Ability': 
                        atributes_dict[key] = value
                    elif key == 'Iniciative': atributes_dict[key] = atributes_dict['Reaction'] + atributes_dict['Intuition']
                    elif key == 'Iniciative_Phases': pass
                    else: 
                        atributes_dict[key] = atributes_dict[key] + dwarf_race_dict[key][3]
                        celk_atributy.append(str(key + " " + str(dwarf_race_dict[key][1]) + " min " + str(dwarf_race_dict[key][0]) + " max " + str(dwarf_race_dict[key][2])))                        
                        if atributes_dict.get(key) < 1:
                            atributes_dict[key] = 1
                            celk_atributy.append(str(key + " " + str(dwarf_race_dict[key][1]) + " min " + str(dwarf_race_dict[key][0]) + " max " + str(dwarf_race_dict[key][2])))
                if m == len(vysl_atr)+2: 
                    print(celk_atributy)
                m += +1
        case metahuman_race_decision if metahuman_race_decision in range(80, 86):
            # this is Orc
            m = 1
            for key, value in orc_race_dict.items():   
                if key != 'BS' and key != 'Iniciative_Phases':
                    if key == 'Metatype' or key == 'Metatype Ability': 
                        atributes_dict[key] = value
                    elif key == 'Iniciative': atributes_dict[key] = atributes_dict['Reaction'] + atributes_dict['Intuition']
                    elif key == 'Iniciative_Phases': pass
                    else: 
                        atributes_dict[key] = atributes_dict[key] + orc_race_dict[key][3]
                        celk_atributy.append(str(key + " " + str(orc_race_dict[key][1]) + " min " + str(orc_race_dict[key][0]) + " max " + str(orc_race_dict[key][2])))                        
                        if atributes_dict.get(key) < 1:
                            atributes_dict[key] = 1
                            celk_atributy.append(str(key + " " + str(orc_race_dict[key][1]) + " min " + str(orc_race_dict[key][0]) + " max " + str(orc_race_dict[key][2])))
                if m == len(vysl_atr)+2: 
                    print(celk_atributy)
                m += +1
        case metahuman_race_decision if metahuman_race_decision in range(0, 81):
            # this is Human
            m = 1
            for key, value in human_race_dict.items():
                if key != 'BS' and key != 'Iniciative_Phases':
                    if key == 'Metatype' or key == 'Metatype Ability': 
                        atributes_dict[key] = value
                    elif key == 'Iniciative': atributes_dict[key] = atributes_dict['Reaction'] + atributes_dict['Intuition']
                    elif key == 'Iniciative_Phases': pass
                    else: 
                        atributes_dict[key] = atributes_dict[key] + human_race_dict[key][3]
                        celk_atributy.append(str(key + " " + str(human_race_dict[key][1]) + " min " + str(human_race_dict[key][0]) + " max " + str(human_race_dict[key][2])))                        
                        if atributes_dict.get(key) < 1:
                            atributes_dict[key] = 1
                            celk_atributy.append(str(key + " " + str(human_race_dict[key][1]) + " min " + str(human_race_dict[key][0]) + " max " + str(human_race_dict[key][2])))
                if m == len(vysl_atr)+2: 
                    print(celk_atributy)                            
                m += +1