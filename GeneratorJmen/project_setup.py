from enum import Enum, auto
import random

from GeneratorJmen.Data.Gods.gods import *
from GeneratorJmen.Data.Name import names
from GeneratorJmen.Data.NickName import nicknames
from GeneratorJmen.Data.Surname import surname
from GeneratorAppearance.Data.Body.body import *
from GeneratorAppearance.Data.Body.head import *
from GeneratorSocial.Data.characteristics import *

#TODO: asi lepe dat zdrojovy kod teto stranky a zkopnout
#    view-source:https://www.character-generator.org.uk/bio/

# TODO: nejdrive generovat gender, sexualni preference, rasu, z jake lidske rasy je, 
# zemi puvodu, pak jmeno a pak dalsi
# TODO: lidske/metalidske rasy predelat samostatne
# TODO: vymyslet jak generovat a z ceho - ? - sehnat data net ? zivotni udalosti
# TODO: rozmyslet si lepe adresarovou strukturu
# TODO: printovat bude jeden soubor k tomu urcenej - pokud soubory ci print dict
# TODO: dodelat testy a kouknout na "navrhove vzory" k priprave na dalsi verzi
# TODO: najit cestu jak testovat vysledne stringy ?AI?, 
# slo by pres docstrings a pod kontrolory jazyka?
# - proste promyslet zda by u neceho nebylo lepsi mit jine datove typy, ci to nepostavit jinak
# zda uz nemyslet na reseni pres soubory, spoustec, linux/windows verzi a ospath pokud bude potreba
# / nabidnu at si vybere cestu
# kaslat na Os a jet pres pipenv
# ve 3. verzi mit klikacku webu kde se to bude generovat a ukladat do pdf a pod - pandas
# ve 4. zapojit tu webovku s AI co napises jakej obrazek a vygeneruje ti jej
# ve 4. zapojit tu webovku s AI (pokud je) co nahodim texty a ono mi to vygeneruje zivotni udalosti
# MEMO: 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 key for an openapi
# MEMO: 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 key for an openapi







    
# print(race_detail_type, 'eye_color is : ', random.choice(race_details[race_detail_type][]['eye_color']))
# print(race_detail_type, 'hair_color is : ', random.choice(race_details[race_detail_type]['hair_color']))
# print(race_detail_type, 'skin_tone is : ', random.choice(race_details[race_detail_type]['skin_tone']))

# TODO: done races 
# class print and choose
# TODO: zakomponovat randomizer z shadowrunu
# http://www.miyako.pro/files/Games/Shadowrun/books/Shadowrun%204th%20Edition%20-%20Anniversary.pdf
# https://wrathofzombie.files.wordpress.com/2012/09/shadowrun-background-generator.pdf
# TODO: zapracovat radek od print(random.choice(list(Tribe_name_origin)).value)
# do radku if x in gods_egypt.intent_gods_about_eg:
    # print(gods_egypt.intent_gods_about_eg[x])

###################################################
# New way
###################################################
# Die Roll Clothes Hairstyle Affections
#  1    Biker Leahter       Mohawk                  Tattoos
#  2    Blue Jeans          Long and Grungy         Kick Ass Attitude Glasses
#  3    Fancy Suit          Punked Out              Glowing Tattoos
#  4    Ripped Clothing     Crazy Colors            Spiked Gloves and Belt
#  5    Hot Shorts          Bald                    Interesting Piercings
#  6    High Fashion        Dreds                   Stretched Ear Piercings
#  7    Military Garb       Cut and Clean           Nail Polish that changes color
#  8    Average Clothes     Shaggy                  High Heels or Platform boots
#  9    80s Retro           Afro                    Crazy Colored Contacts
#  10   Costume             Long and Straight       Scarification Art


# 2) Ethnic Origins
# 1 Anglo-American
# 2 African
# 3 European
# 4 Japanese/Koren
# 5 Chinese/Southern Asia
# 6 Pacific Islander
# 7 Hispanic-American
# 8 South American
# 9 Black American
# 10 Central European


# make_list = list(Body_shape)
# BODY_SHAPE = random.sample(make_list, 2)
# BODY_SHAPE = (BODY_SHAPE[0].value, BODY_SHAPE[1].value)


# print(random.choice(tuple(Tribe_name_origin)).value)
# print(random.choice(tuple(Tribe_surname_origin)).value)

print(SEXUAL_PREFERENCY_LIST)
print(SOCIAL_CLASS)
print(POSITIVE_CHARACTERISTIC)
print(HEIGHT)
print(WEIGHT)
print(BODY)
print(BODY_SHAPE)

value = random.choice(list(Hair_types))
print (value.value)
