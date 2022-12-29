###TODO: prekopat a dat tam static methody a spol


# kód neumí ohlídat rozdělení všech bodů, pouze hlídá zápornou hodnotu bodů na rozdělení

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
    choose_destiny: int = random.randint(1, 10)
    atributgen: int
    pointspool: int         # na platbu za edge, rasu a skilly
    pointspool_atr = 200 + (len(listatr)*10)
    max: int = len(listatr)
    print('Počáteční body na rozdělení:', (pointspool_atr - 80))
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
            pointspool_atr = 200 + (len(listatr)*10)
            atributgen = 0
            max = len(listatr) + 1
    if choose_destiny is None:
            pointspool_atr = 200 + (len(listatr)*10)
            atributgen = 0
            max = len(listatr) + 1
    result = [atributgen, pointspool_atr, max]
    #print('Stav bodu:', pointspool)
    return result


def make_atributes_loop():
    i: int = 1
    decision = make_decision()
    atributgen = int(decision[0])
    pointspool_atr = int(decision[1])
    max = int(decision[2])
    while i < max:
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

        if i==1: atributgen = random.randint(4, 6)
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

    metahuman_race_decision = random.randint(100, 100)
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
                        if atributes_dict.get(key) < 1:
                            atributes_dict[key] = 1
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
                        if atributes_dict.get(key) < 1:
                            atributes_dict[key] = 1
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
                        if atributes_dict.get(key) < 1:
                            atributes_dict[key] = 1
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
                        if atributes_dict.get(key) < 1:
                            atributes_dict[key] = 1
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
                        if atributes_dict.get(key) < 1:
                            atributes_dict[key] = 1
                m += +1