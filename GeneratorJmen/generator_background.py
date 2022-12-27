from GeneratorJmen.setup_generator import *
from project_values_setup import *

import random

def write_results():
    #TODO list
    #Todays is only for set uped languages
    tribe_name_origin = tribe_name_origin_input()
    tribe_surname_origin = tribe_surname_origin_input()
    nickname = nickName_rand.list_of_intents_tribe_nickNames()
    
    if tribe_name_origin is not None or tribe_surname_origin is not None:
        print(tribe_name_origin + " \"" + nickname + "\" " + tribe_surname_origin)
        print(god_rand.list_of_intents_tribe_gods())

        #########################################################################
        #### TAKTO TO HEZKY FUNGUJE VE SLOVNIKU S POLEM
        #########################################################################
        # rasa = random.choice(rase_choice)
        # oci = random.choice(race_details[rasa][1])
        # print(random.choice(oci))

    else:        
        print(
            name_rand.list_of_intents_tribe_names() 
            + " \"" + nickName_rand.list_of_intents_tribe_nickNames() + "\" " +
            surname_rand.list_of_intents_tribe_surname()
            )
        print(god_rand.list_of_intents_tribe_gods())

@staticmethod
def gender_input():
    #TODO: jak setupovat vse
    #HINT: pouzit oop nadefinovat si tridou a pak tam davat hodnotu
    #set_name_by_tribe zda bylo pozadovano z jakych tribes je jmeno a prijmeni 
    #TODO: gender pozdeji
    # potom odkomentovat IF
    gender = 1
    # gender: int
    # if gender == 1 or gender == 2:
    #     if gender == 1:
    #         gender = Gender.male
    #     if gender == 2:
    #         gender = Gender.female    
    # elif gender not in range(1,2):
    #     raise NameError('Oops! You type: ' + gender + ' That was no valid number. Valid number is 1 or 2 Try again...')
    return gender



@staticmethod
def tribe_name_origin_input():
    chosen_tribe_name = random.randint(1,8)
    gender = gender_input()
    match chosen_tribe_name:
        case 1 : tribe_name_origin = random.choice(intent_names_pl)
        case 2 : tribe_name_origin = random.choice(intent_names_ne)
        case 3 : tribe_name_origin = random.choice(intent_names_es)
        case 4 : tribe_name_origin = random.choice(intent_names_fr)
        case 5 : tribe_name_origin = random.choice(intent_names_gk)
        case 6 : tribe_name_origin = random.choice(intent_names_it)
        case 7 : tribe_name_origin = random.choice(intent_names_us)
        case 8 : tribe_name_origin = random.choice(intent_names_cz[gender])
    return tribe_name_origin

@staticmethod
def tribe_surname_origin_input():
    tribe_surname_origin = random.randint(1,8)
    match tribe_surname_origin:
        case 1 : tribe_surname_origin = random.choice(intent_surname_pl)
        case 2 : tribe_surname_origin = random.choice(intent_surname_ne)
        case 3 : tribe_surname_origin = random.choice(intent_surname_es)
        case 4 : tribe_surname_origin = random.choice(intent_surname_fr)
        case 5 : tribe_surname_origin = random.choice(intent_surname_gk)
        case 6 : tribe_surname_origin = random.choice(intent_surname_it)
        case 7 : tribe_surname_origin = random.choice(intent_surname_us)
        case 8 : tribe_surname_origin = random.choice(intent_surname_cz)
    return tribe_surname_origin
