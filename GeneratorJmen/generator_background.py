from GeneratorJmen.setup_generator import *

import random

#TODO: jak setupovat vse
#set_name_by_tribe zda bylo pozadovano z jakych tribes je jmeno a prijmeni 
set_tribe_name = ""
set_tribe_surname = ""
set_tribe_NickName = ""
set_tribe_gods = "" 

class generator_of_full_name:
    #TODO list
    #Todays is only for set uped languages
    if set_tribe_name != "" and set_tribe_surname != "" and set_tribe_NickName != "" and set_tribe_gods != "":
        # dodelat
        # if set_tribe_name == surname_rand.list_of_intents_tribe_surname()[surname_rand.list_of_intents_tribe_surname()[1]]:
        #     pass
        #nutno dodelat
        print(
            str(random.choice(name_rand.list_of_intents_tribe_names())) 
            + " \"" + str(random.choice(nickName_rand.list_of_intents_tribe_nickNames())) + "\" " + 
            str(random.choice(surname_rand.list_of_intents_tribe_surname()))
            )
        print(god_rand.list_of_intents_tribe_gods())

        pass
    else:

        print(
            str(random.choice(name_rand.list_of_intents_tribe_names())) 
            + " \"" + str(random.choice(nickName_rand.list_of_intents_tribe_nickNames())) + "\" " + 
            str(random.choice(surname_rand.list_of_intents_tribe_surname()))
            )
        print(god_rand.list_of_intents_tribe_gods())



