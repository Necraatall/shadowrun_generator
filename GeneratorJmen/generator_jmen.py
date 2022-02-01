from GeneratorJmen.setup_name_generator import *

import random

#TODO: jak setupovat vse
#set_name_by_tribe zda bylo pozadovano z jakych tribes je jmeno a prijmeni 
set_name_by_tribe = False

class generator_of_full_name:
    if set_name_by_tribe != False:
        #nutno dodelat
        pass
    else:
        #chosen_god = str(random.choice(god_rand.list_of_intents_tribe_gods()[0]))
        #chosen_god_about = str(intent_gods_about_gk[chosen_god])
        print(
            str(random.choice(name_rand.list_of_intents_tribe_names())) 
            + " " + str(random.choice(nickName_rand.list_of_intents_tribe_nickNames())) + " " + 
            str(random.choice(surname_rand.list_of_intents_tribe_surname()))
            )
        print(god_rand.list_of_intents_tribe_gods())
        # print(
        #     " " + 
        #     chosen_god
        #     + " neco o nem: " + 
        #     chosen_god_about
        #     + "."
        # )


