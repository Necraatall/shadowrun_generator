from enum import Enum
import random


class Height(Enum):
    VERY_TALL_HEIGHT = "very tall"
    TALL_HEIGHT = "tall"
    AVERAGE_HEIGHT = "average height"
    SHORT_HEIGHT = "short"
    VERY_SHORT_HEIGHT ="very short"

make_list = list(Height)
HEIGHT = random.choice(make_list)
HEIGHT = (HEIGHT.value)

class Weight(Enum):
    VERY_OVERWEIGHT_WEIGHT = "very overweight"
    OVERWEIGHT_WEIGHT = "overweight"
    AVERAGE_WEIGHT = "average weight"
    UNDERWEIGHT_WEIGHT = "underweight"
    VERY_UNDERWEIGHT_WEIGHT = "very underweight"
    BIG_WEIGHT = "big"
    HEAVYSET_WEIGHT = "heavyset weight"
    THIN_WEIGHT = "thin weight"

make_list = list(Weight)
WEIGHT = random.choice(make_list)
WEIGHT = (WEIGHT.value)

age_appearance = random.randrange(0, 2, 1)
physical_age = random.randrange(6, 60, 1)
psychical_age = 0
if age_appearance == 0:
    psychical_age = random.randrange((physical_age//2), (physical_age - (physical_age//4)+1), 1)
    appearence_age = random.randrange((physical_age//2), (physical_age - (physical_age//3)+1+3), 1)
else: 
    psychical_age = random.randrange((physical_age//2), (physical_age + (physical_age//4)-1), 1)
    appearence_age = random.randrange((physical_age//2), (physical_age + (physical_age//3)-1+3), 1)


class Age(Enum):
    PHYSICAL_AGE = physical_age
    PSYCHICAL_AGE = psychical_age
    APPEARENCE_AGE = appearence_age


class Body(Enum):
    VERY_WELL_BUILT_BODY = "very well-built"
    WELL_BUILD_BODY = "well-built"
    AVERAGE_BUILD_BODY = "average build"
    FINE_BUILD_BODY = "fine build"
    VERY_FINE_BUILD_BODY = "very fine build"
    SKINNY_BUILD_BODY = "skinny build"
    SLENDER_BUILD_BODY = "slender build"

make_list = list(Body)
BODY = random.choice(make_list)
BODY = (BODY.value)

class Body_shape(Enum):
    BOTTOM_HOURGLASS = "bottom hourglass"
    INVERTED_TRINGLE = "inverted tringle"
    DIAMOND = "diamond"
    ATHLETIC = "athletic"
    ROUND = "round"
    RECTANGLE = "rectangle"
    TRIANGLE = "triangle"
    HOURGLASS = "hourglass"
    PEAR = "pear"
    APPLE = "apple"
    TRAPEZOID = "trapezoid"

make_list = list(Body_shape)
BODY_SHAPE = random.choice(make_list)
BODY_SHAPE = (BODY_SHAPE.value)


eye_color = ('brown', 'black', 'blue', 'green', 'yellow')
hair_color = ('auburn', 'brown', 'black', 'blonde', 'copper', 'ginger', 'golden', 'grey', 'mouse', 'red', 'dark brown', 'white')
skin_tone = ('almond', 'brown', 'bronze', 'chocolate', 'cocoa', 'dark chocolate', 'fair', 'light', 'olive', 'pale', 'walnut')

# race_choice = "Europoidic"
race_choice = random.choice(('Europoidic', 'Caucasian', 'Latino/Hispanic', 'African', 'Caribbean', 'Middle_Eastern', 'South_Asian', 'East_Asian', 'Mixed'))
if race_choice == 'Europoidic':
    sub_race_europoidic_choice = random.choice(('Nordic', 'Falian', 'Baltic', 'Mediterran', 'Dinaric', 'Alpine'))
if race_choice == 'Middle_Eastern':
    sub_race_middle_eastern_choices = random.choice(('Hamitic', 'Sudeten', 'Oriental'))
if race_choice == 'African':
    sub_race_african_choice = random.choice(('Hamitic'))

race_details = {
    'Europoidic' : {
        "Nordic" : {
            "Vzrůst" : random.choice(("vysoký", "štíhlý")),
            "Postava" : "atletická (respiratorní), široká ramena, pevné držení těla",
            "Končetiny" : "dlouhé ruce a nohy",
            "Tělesná_výška" : "175",
            "Pigmentace" : "světle " + random.choice(("bílá", "narůžovělá, jemná")) + " pleť",
            "Nos" : "dlouhý, úzký, " + random.choice(("rovný", "zahnutý")),
            "Rty" : "tenké",
            "Vlasy" : "světlé " + random.choice(("jemné", "rovné", "vlnité")) + " barvy "
                + random.choice(("šedá", "myší", "zlatá", "blond", "bílá")),
            "Oči" : "světle " + random.choice(("modré", "zelené", "šedé")),
            "Obličej" : "úzký, vysoký",
            "Brada" : random.choice(("úzká", "hranatá", "ostrá")),
            "Lebka" : "dlouhá (dolichocefalie) – lebeční index 75-75,5, obličejový index nad 90",
            "Čelo" : "Ploché, úzké, dozadu sklopené ",
            "Čelist" : "dobře vyvinutá brada",
            "Oblast" : random.choice((
                "severní Evropa",
                "Skandinávský poloostrov",
                "Pobaltí",
                "část Finska",
                "Estonska",
                "Lotyšska a Litvy",
                "severozápadní Polsko",
                "severní Německo",
                "Velká Británie",
                "Irsko",
                "severní Skotsko",
                "Holandsko",
                "Belgie",
                "severní Francie",
                "severní Rusko",
            ))
        },
        "Falian" : {
            "Vzrůst" : "vysoký",
            "Postava" : "robustní, statná (spíše digestivní)",
            "Pigmentace" : "světle bílá",
            "Nos" : "středně široký",
            "Rty" : "tenké",
            "Vlasy" : "světlé",
            "Oči" : "světlé",
            "Obličej" : "široký, poněkud čtvercovitý",
            "Lebka" : "dlouhá (dolichocefalie), lebeční index kolem 75",
            "Čelo" : "strmé, široké, velmi vyvinuté nadočnicové oblouky",
            "Čelist" : "široká a masivní s vystouplou bradou",
            "Oblast" : random.choice((
                "Vestfálsko",
                "střední Švédsko")),
        },
        "Baltic" : {
            "Vzrůst" : random.choice(("malý", "střední")),
            "Postava" : "podsaditá, rovná, široká ramena (digestivní)",
            "Končetiny" : "krátké",
            "Tělesná_výška" : "164",
            "Krk" : "široký, krátký",
            "Pigmentace" : random.choice(("světlá", "žlutošedá")),
            "Nos" : random.choice(("krátký", "mělký")),
            "Vlasy" : random.choice(("pevné", "rovné")) + random.choice(("popelavé", "světlý blond")),
            "Oči" : random.choice(("světle modré", "modrobílé")) + "posazeny daleko od sebe, někdy i polo-mongoloidní tvar",
            "Obličej" : "robustní, široký, vysedlé lícní kosti",
            "Lebka" : "krátká (brachycefalie) – lebeční index 80,9-83,2 ",
            "Čelist" : "masivní s nevystupující bradou",
            "Brada" : random.choice(("kulatá", "ustupující")),
            "Čelo" : "dozadu sklopené",
            "Oblast" : random.choice((
                "východní Evropa" 
                "střední a jižní Polsko",
                "Pobaltí " + random.choice(("Litva", "Lotyšsko", "Estonsko")),
                "Česko",
                "Slovensko",
                "Maďarsko",
                "Ukrajina",
                "Bělorusko",
                "Finsko",
                "Rusko",
                "Skandinávie",
                "Holandsko",
            ))
        },
        "Mediterran" : {
            "Vzrůst" : "nízký",
            "Postava" : "štíhlá (respiratorní), držení pružné",
            "Končetiny" : "v poměru k tělu dlouhé",
            "Tělesná_výška" : "161",
            "Pigmentace" : "hnědobílá",
            "Nos" : random.choice(("rovný", "vysoký", "úzký")) + "s vysokým hřbetem",
            "Rty" : "trochu výraznější oproti nordickému typu",
            "Vlasy" : "tmavé",
            "Čelo" : random.choice(("více strmé a klenuté", "úzké")),
            "Oči" : "tmavě hnědé",
            "Obličej" : "oválný",
            "Brada" : "úzká",
            "Lebka" : "dlouhá (dolichocefalie) – lebeční index 70-75, obličejový index nad 90",
            "Oblast" : random.choice((
                "jižní a západní Evropa",
                "Středomoří",
                "Pádská nížina",
                "pobřeží Černého moře",
                "Španělsko",
                "Portugalsko", 
                "Řecko",
                "část Walesu",
                "jihozápadní Německo",
                "jižní Polsko",
                "částečně jižní a centrální Rusko či Balkán",
            ))
        },
        "Dinaric" : {
            "Vzrůst" : "vysoký",
            "Postava" : "štíhlá, astenická (respiratorní) s nenuceným držením těla",
            "Končetiny" : "dlouhé nohy, kratší ruce",
            "Tělesná_výška" : "174",
            "Krk" : "dlouhý",
            "Pigmentace" : random.choice(("hnědobílá", "tmavší")),
            "Nos" : random.choice(("velký", "úzký", "vysoký", "orlí (konvexní)")),
            "Vlasy" : "silné " + random.choice(("tmavohnědé", "černé")),
            "Oči" : random.choice(("tmavohnědé", "černé")),
            "Uši" : "velké",
            "Obličej" : "úzký, vystouplé lícní kosti",
            "Čelo" : "trochu dozadu sklopené",
            "Lebka" : "krátká (brachycefalie) se zploštělým, ale zakulaceným týlem – lebeční index 85-87, obličejový index 90-93",
            "Čelo" : "relativně vysoké, šikmé, rozvinuté nadočnicové oblouky",
            "Čelist" : "nevýrazná brada",
            "Brada" : random.choice(("široká", "kulatá", "vysoká")),
            "Oblast" : random.choice((
                "jihovýchodní Evropa",
                "Balkánský poloostrov",
                "Chorvatsko",
                "Srbsko",
                "Černá Hora",
                "Bosna a Hercegovina",
                "Albánie",
                "Slovinsko",
                "Bulharsko",
                "Makedonie",
                "Karpaty",
                "Rumunsko",
                "Slovensko",
                "západní Ukrajina",
                "severozápadní Itálie",
                "východní a západní Alpy",
                "Švýcarsko",
                "střední Francie",
                "Pyreneje",
                "Polsko",
                "jižní Německo",
            ))
        },
        "Alpine" : {
            "Vzrůst" : "malý",
            "Tělesná_výška" : "163",
            "Postava" : "podsaditá (digestivní), těžkopádné",
            "Končetiny" : "krátké",
            "Pigmentace" : random.choice(("žlutohnědá", "o něco tlustší")),
            "Nos" : random.choice(("krátký" "tupý")),
            "Vlasy" : "tlusté, pevné " + random.choice(("tmavohnědé", "černé")),
            "Oči" : "tmavohnědé",
            "Obličej" : "široký, kulatý",
            "Lebka" : "krátká (brachycefalie) – lebeční index 84-87, obličejový index nad 80",
            "Čelo" : random.choice(("strmé", "klenuté", "kulaté", "široké")),
            "Čelist" : "široká",
            "Brada" : random.choice(("tupá", "zaoblená")),
            "Oblast" : random.choice(( 
                "střední Evropa",
                "západní Evropa",
                "západní Alpy", 
                "střední Francie",
                "Rakousko",
                "Česko",
                "Švýcarsko",
                "střední Itálie",
                "Slovinsko",
                "jižní Německo",
                "jihozápadní Německo",
                "Maďarsko",
                "jižní Polsko",
            ))
        }

    },
    'Middle_Eastern' : {
        'Hamitic' : {
            "Vzrůst" : "střední",
            "Postava" : "podsaditá (digestivní)",
            "Končetiny" : "krátké",
            "Pigmentace" : "snědá - barvy " + random.choice(("mandle", "olivy", "vlašský ořech")),
            "Nos" : "zahnutý, masitý směrem dolů (podobá se číslici 6)",
            "Rty" : "masité, dolní ret je větší než horní",
            "Vlasy" : "tmavě " + random.choice(("hnědé", "černé", "šedé")) + ", kudrnaté, obočí často srostlé",
            "Oči" : "tmavě " + random.choice(("hnědé", "černé", "zelené")) + ", odhalená vrchní oční víčka (nevyvinuté nadočnicové oblouky)",
            "Uši" : "velké",
            "Obličej" : "středně široký, vystouplé lícní kosti",
            "Lebka" : "krátká (brachycefalie) se zploštělým týlem",
            "Čelo" : "nízké, šikmé, kulaté",
            "Čelist" : "nízká, ustupující brada",
            "Oblast" : random.choice((
                "Blízký východ (Malá Asie)",
                "Kavkaz",
                "Arménie",
                "Asýrie",
                "Ázerbájdžán",
                "Gruzie",
                "Libanon a Sýrie",
            ))
        },
        'Sudeten' : {
            "Vzrůst": "malý",
            "Pigmentace": "tmavší - barvy " + random.choice(("mandle", "olivy", "vlašský ořech")),
            "Nos": "široký, plochý",
            "Vlasy": "tmavě " + random.choice(("hnědé", "černé", "šedé")),
            "Oči": "tmavě " + random.choice(("hnědé", "zelené")),
            "Obličej": "středně široký, výrazné lícní kosti",
            "Lebka": "střední (mesocefalie)",
            "Čelist": "nevystupující brada",
            "Oblast": "východní Evropa",
        },
        'Oriental' : {
            "Vzrůst" : "malý až střední",
            "Postava" : "štíhlá (respiratorní)",
            "Pigmentace" : "snědá - barvy " + random.choice(("mandle", "olivy", "vlašský ořech")),
            "Nos" : "úzký, vysoký",
            "Rty" : "plné",
            "Vlasy" : "tmavě " + random.choice(("hnědé", "černé", "šedé")),
            "Oči" : "tmavě " + random.choice(("hnědé", "černé", "zelené")),
            "Obličej" : "vysoký, převážně úzký a rovný",
            "Lebka" : "dlouhá (dolichocefalie)",
            "Oblast" : random.choice((
                "severní Afrika",
                "Blízký východ",
                "Arábie",
                "Libanon",
                "Irák",
                "Sýrie",
                "Turecko",
                "Degestán a Írán",
            ))
        }
    },
    'African' : {
        'Hamitic' : {
            "stature" : "medium",
            "build" : "stocky",
            "Limbs" : "short",
            "Pigmentation" : "brown - color" + random.choice(("almond", "olive", "walnut")),
            "Nose" : "straight",
            "Lips" : "fleshy",
            "Hair" : "dark" + random.choice(("brown", "black", "grey")) + ", curly, eyebrows often knitted",
            "Eyes" : "dark " + random.choice(("brown", "black")),
            "Ears" : "large",
            "Face" : "tall",
            "Skull" : "long (dolichocephaly)",
            "Forehead" : "low, round",
            "Jaw" : "low, receding chin",
            "area" : random.choice((
                "North Africa",
                "East Africa",
                "southern Africa",
            ))
        }
    },
    'Caribbean' : {
        "eye_color" : random.choice((eye_color[0], eye_color[1],eye_color[3])),
        "hair_color" : random.choice((hair_color[1],hair_color[2],hair_color[7])),
        "skin_tone" : random.choice((skin_tone[10], skin_tone[4],skin_tone[3],skin_tone[5]))
    },
    'Latino/Hispanic' : {
        "eye_color" : random.choice((eye_color[0], eye_color[2], eye_color[3])), 
        "hair_color" : random.choice((hair_color[1],hair_color[2],hair_color[7])),
        "skin_tone" : random.choice((skin_tone[10], skin_tone[4], skin_tone[3],skin_tone[5], skin_tone[10]))
    },
    'Caucasian' : {
        "eye_color" : random.choice((eye_color[0], eye_color[2], eye_color[3])),
        "hair_color" : hair_color,
        "skin_tone" : random.choice((skin_tone[9], skin_tone[9],skin_tone[8],skin_tone[7],skin_tone[2]))
    },
    'South_Asian' : {
        "eye_color" : random.choice((eye_color[0], eye_color[1])),
        "hair_color" : random.choice((hair_color[1],hair_color[2],hair_color[7])),
        "skin_tone" : random.choice((skin_tone[10], skin_tone[8],skin_tone[1]))
    },
    'East_Asian' : {
        "eye_color" : random.choice((eye_color[0], eye_color[1])),
        "hair_color" : random.choice((hair_color[10], hair_color[2],hair_color[7], hair_color[11])),
        "skin_tone" : random.choice((skin_tone[9], skin_tone[6], skin_tone[7] ,skin_tone[1]))
    },
    'Mixed' : {random.choice((
        'Mestic - descendant of a European and a Native American Indian',
        'Mulat - the offspring of a white man and a black man',
        'Zambaigo - descendant of an East Asian and a Native American/Eskimo',
        'Zambo - descended from a black man and a Native American',
        'Kajot - descendant of a mestizo and a mulatto',
        )):
        {
        "eye_color" : (eye_color),
        "hair_color" : random.choice((hair_color[1],hair_color[2],hair_color[7],hair_color[3],hair_color[9])),
        "skin_tone" : random.choice((skin_tone[9], skin_tone[6], skin_tone[7] ,skin_tone[2], skin_tone[2], skin_tone[8], skin_tone[3]))
    }}
}

if any(s in race_choice for s in ('Caribbean', 'Latino/Hispanic', 'Caucasian', 'South_Asian', 'East_Asian', 'Mixed')):
    race_chosen=race_details[race_choice]
    # print("\n", race_details[race_choice].items(), "\n")
else: 
    race_chosen=random.choice(list(race_details[race_choice].items()))
    # print(random.choice(list(race_details[race_choice].items())), "\n")

