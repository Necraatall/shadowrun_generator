from asyncio.windows_events import NULL
from GeneratorJmen.setup_generator import *
from project_values_setup import *

import random

def tribe_name_origin_input():
    tribe_name_origin = 1
    match tribe_name_origin:
        case 1 :
            tribe_name_origin = random.choice(intent_names_pl)
        case 2 :
            tribe_name_origin = random.choice(intent_names_ne)
        case 3 :
            tribe_name_origin = random.choice(intent_names_es)
        case 4 :
            tribe_name_origin = random.choice(intent_names_fr)
        case 5 :
            tribe_name_origin = random.choice(intent_names_gk)
        case 6 :
            tribe_name_origin = random.choice(intent_names_it)
        case 7 :
            tribe_name_origin = random.choice(intent_names_us)
    return tribe_name_origin

def tribe_surname_origin_input():
    tribe_surname_origin = 1
    match tribe_surname_origin:
        case 1 :
            tribe_surname_origin = random.choice(intent_surname_pl)
        case 2 :
            tribe_surname_origin = random.choice(intent_surname_ne)         
        case 3 :
            tribe_surname_origin = random.choice(intent_surname_es)
        case 4 :
            tribe_surname_origin = random.choice(intent_surname_fr)         
        case 5 :
            tribe_surname_origin = random.choice(intent_surname_gk)
        case 6 :
            tribe_surname_origin = random.choice(intent_surname_it)
        case 7 :
            tribe_surname_origin = random.choice(intent_surname_us)    

def genre_input():
    #TODO: jak setupovat vse
    #HINT: pouzit oop nadefinovat si tridou a pak tam davat hodnotu
    #set_name_by_tribe zda bylo pozadovano z jakych tribes je jmeno a prijmeni 
    #TODO: gender pozdeji
    # potom odkomentovat IF
    #gender: int
    # if gender == 1 or gender == 2:
    #     if gender == 1:
    #         gender = Gender.male
    #     if gender == 2:
    #         gender = Gender.female    
    # elif gender not in range(1,2):
    #     raise NameError('Oops! You type: ' + gender + ' That was no valid number. Valid number is 1 or 2 Try again...')
    pass

def define_inputs():
    #TODO list
    #Todays is only for set uped languages
    if tribe_name_origin_input() is not NULL or tribe_surname_origin_input() is not NULL:
        name = str(tribe_name_origin_input())
        surname = str(tribe_surname_origin_input())

        print(
                name
                + " \"" + nickName_rand.list_of_intents_tribe_nickNames() + "\" " +
                surname
            )
        print(god_rand.list_of_intents_tribe_gods())

    else:
        
        print(
            name_rand.list_of_intents_tribe_names() 
            + " \"" + nickName_rand.list_of_intents_tribe_nickNames() + "\" " +
            surname_rand.list_of_intents_tribe_surname()
            )
        print(god_rand.list_of_intents_tribe_gods())



