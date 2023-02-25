from enum import Enum
import random


class Height(Enum):
    VERY_TALL_HEIGHT = "very tall"
    TALL_HEIGHT = "tall"
    AVERAGE_HEIGHT = "average height"
    SHORT_HEIGHT = "short"
    VERY_SHORT_HEIGHT ="very short"


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

class Height(Enum):
    VERY_TALL_HEIGHT = "very tall"
    TALL_HEIGHT = "tall"
    AVERAGE_HEIGHT = "average height"
    SHORT_HEIGHT = "short"
    VERY_SHORT_HEIGHT ="very short"

make_list = list(Weight)
WEIGHT = random.choice(make_list)
WEIGHT = (WEIGHT.value)

race_details = {
    'Europoidic' : {
        "Nordic" : {
            "Stature" : random.choice(("tall", "slim")),
            "Build" : "athletic (respiratory), broad shoulders, strong posture",
            "Limbs" : "long arms and legs",
            "Body_height" : "175",
            "Pigmentation" : "pale " + random.choice(("white", "pinkish, delicate")) + "complexion",
            "Nose" : "long, narrow, " + random.choice(("straight", "curvy")),
            "Rty" : "thin",
            "Hair" : "light " + random.choice(("fine", "straight", "wavy")) + " colors "
                + random.choice(("grey", "mouse", "gold", "blonde", "white")),
            "Eyes" : "light " + random.choice(("blue", "green", "gray")),
            "Face" : "narrow, tall",
            "Chin" : random.choice(("narrow", "square", "sharp")),
            "Skull" : "long (dolichocephaly) - cranial index 75-75.5, facial index over 90",
            "Forehead" : "Flat, narrow, posteriorly tilted",
            "Jaw" : "well-developed chin",
            "Region" : random.choice((
                "Northern Europe",
                "Scandinavian Peninsula",
                "Baltic States",
                "part of Finland",
                "Estonia",
                "Latvia and Lithuania",
                "north-western Poland",
                "northern Germany",
                "Great Britain",
                "Ireland",
                "northern Scotland",
                "Holland",
                "Belgium",
                "northern France",
                "northern Russia",
            ))
        },
        "Falian" : {
            "Stature" : "tall",
            "Build" : "robust, sturdy (rather digestive)",
            "Pigmentation" : "pale white",
            "Nose" : "medium wide",
            "Rty" : "thin",
            "Hair" : "light",
            "Eyes" : "light",
            "Face" : "broad, somewhat square",
            "Skull" : "long (dolichocephaly), cranial index about 75",
            "Forehead" : "steep, broad, very developed supraorbital arches",
            "Jaw" : "broad and massive with a prominent chin",
            "Region" : random.choice((
                "Westphalia",
                "Central Sweden")),
        },
        "Baltic" : {
            "Stature" : random.choice(("small", "medium")),
            "Build" : "stocky, straight, broad shoulders (digestive)",
            "Limbs" : "short",
            "Body_height" : "164",
            "Krk" : "wide, short",
            "Pigmentation" : random.choice(("light", "yellow-gray")),
            "Nose" : random.choice(("short", "shallow")),
            "Hair" : random.choice(("solid", "straight")) + random.choice(("ashy", "light blonde")),
            "Eyes" : random.choice(("light blue", "blue-white")) + "set far apart, sometimes semi-mongoloid shape",
            "Face" : "robust, broad, prominent cheekbones",
            "Skull" : "short (brachycephaly) - cranial index 80,9-83,2 ",
            "Jaw" : "massive with non-protruding chin",
            "Chin" : random.choice(("round", "receding")),
            "Forehead" : "posteriorly tilted",
            "Region" : random.choice((
                "Eastern Europe" 
                "Central and Southern Poland",
                "Baltic States" + random.choice(("Lithuania", "Latvia", "Estonia")),
                "Czech Republic",
                "Slovakia",
                "Hungary",
                "Ukraine",
                "Belarus",
                "Finland",
                "Russia",
                "Scandinavia",
                "Holland",
            ))
        },
        "Mediterran" : {
            "Stature" : "low",
            "Build" : "slender (respiratory), posture flexible",
            "Limbs" : "long in proportion to the body",
            "Body_height" : "161",
            "Pigmentation" : "brown and white",
            "Nose" : random.choice(("straight", "tall", "narrow")) + "high-backed",
            "Rty" : "a little more pronounced than the Nordic type",
            "Hair" : "dark",
            "Forehead" : random.choice(("more steep and arched", "narrow")),
            "Eyes" : "dark brown",
            "Face" : "oval",
            "Chin" : "narrow",
            "Skull" : "long (dolichocephaly) - cranial index 70-75, facial index over 90",
            "Region" : random.choice((
                "South Europe",
                "Western Europe"
                "Mediterranean",
                "Po Plain",
                "Black Sea coast",
                "Spain",
                "Portugal", 
                "Greece",
                "part of Wales",
                "south-west Germany",
                "southern Poland",
                "parts of southern and central Russia or the Balkans",
            ))
        },
        "Dinaric" : {
            "Stature" : "tall",
            "Build" : "slender, asthenic (respiratory) with a casual posture",
            "Limbs" : "long legs, shorter arms",
            "Body_height" : "174",
            "Krk" : "long",
            "Pigmentation" : random.choice(("brownish-white", "darker")),
            "Nose" : random.choice(("large", "narrow", "tall", "eagle (convex)")),
            "Hair" : "thick " + random.choice(("dark brown", "black")),
            "Eyes" : random.choice(("dark brown", "black")),
            "Uši" : "large",
            "Face" : "narrow, prominent cheekbones",
            "Skull" : "short (brachycephaly) with flattened but rounded occiput - cranial index 85-87, facial index 90-93",
            "Forehead" : "slightly posteriorly tilted, relatively high, oblique, well-developed supraorbital arches",
            "Jaw" : "bland chin",
            "Chin" : random.choice(("wide", "round", "high")),
            "Region" : random.choice((
                "Southeast Europe",
                "Balkan Peninsula",
                "Croatia",
                "Serbia",
                "Montenegro",
                "Bosnia and Herzegovina",
                "Albania",
                "Slovenia",
                "Bulgaria",
                "Macedonia",
                "Carpathians",
                "Romania",
                "Slovakia",
                "Western Ukraine",
                "Northwest Italy",
                "Eastern and Western Alps",
                "Switzerland",
                "central France",
                "Pyrenees",
                "Poland",
                "southern Germany",
            ))
        },
        "Alpine" : {
            "Stature" : "small",
            "Body_height" : "163",
            "Build" : "stocky (digestive), cumbersome",
            "Limbs" : "short",
            "Pigmentation" : random.choice(("yellow-brown", "slightly fatter")),
            "Nose" : random.choice(("short", "blunt")),
            "Hair" : "thick, solid" + random.choice(("dark brown", "black")),
            "Eyes" : "dark brown",
            "Face" : "wide, round",
            "Skull" : "short (brachycephaly) - cranial index 84-87, facial index over 80",
            "Forehead" : random.choice(("steep", "arched", "round", "wide")),
            "Jaw" : "wide",
            "Chin" : random.choice(("blunt", "rounded")),
            "Region" : random.choice(( 
                "Central Europe",
                "Western Europe",
                "Western Alps", 
                "Central France",
                "Austria",
                "Czechia",
                "Switzerland",
                "central Italy",
                "Slovenia",
                "southern Germany",
                "Southwest Germany",
                "Hungary",
                "southern Poland",
            ))
        }

    },
    'Middle_Eastern' : {
        'Hamitic' : {
            "Stature" : "medium",
            "Build" : "stocky",
            "Limbs" : "short",
            "Pigmentation" : "brown - color" + random.choice(("almond", "olive", "walnut")),
            "Nose" : "curved, fleshy downward (resembles a 6)",
            "Lips" : "fleshy, lower lip larger than upper lip",
            "Hair" : "dark" + random.choice(("brown", "black", "grey")) + ", curly, eyebrows often knitted",
            "Eyes" : "dark " + random.choice(("brown", "black", "green")) + ", droopy upper eyelid(undeveloped supraorbital arches)",
            "Ears" : "large",
            "Face" : "medium width, prominent cheekbones",
            "Skull" : "short (brachycephaly) with flattened occiput",
            "Forehead" : "low, sloping, round",
            "Jaw" : "low, receding chin",
            "Region" : random.choice((
                "Middle East (Asia Minor)",
                "Caucasus",
                "Armenia",
                "Assyria",
                "Azerbaijan",
                "Georgia",
                "Lebanon and Syria",
            ))
        },
        'Sudeten' : {
            "Stature": "small",
            "Body_height" : "163",
            "Pigmentation": "darker - colors" + random.choice(("almond", "olive", "walnut")),
            "Nose": "wide, flat",
            "Hair": "dark" + random.choice(("brown", "black", "gray")),
            "Eyes": "dark " + random.choice(("brown", "green")),
            "Face": "medium width, prominent cheekbones",
            "Skull": "medium (mesocephaly)",
            "Jaw": "no protruding chin",
            'Region': 'Eastern Europe',
        },
        'Oriental' : {
            "Stature" : "small to medium",
            "Build" : "slender (respiratory)",
            "Pigmentation" : "brown - colors" + random.choice(("almond", "olive", "walnut")),
            "Nose" : "narrow, high",
            "Lips" : "full",
            "Hair" : "dark" + random.choice(("brown", "black", "gray")),
            "Eyes" : "dark " + random.choice(("brown", "black", "green")),
            "Face" : "tall, mostly narrow and straight",
            "Skull" : "long (dolichocephaly)",
            "Region" : random.choice((
                "North Africa",
                "Middle East",
                "Arabia",
                "Lebanon",
                "Iraq",
                "Syria",
                "Turkey",
                "Degestan and Iran",
            ))
        }
    },
    'African' : {
        'Hamitic' : {
            "Stature" : "medium",
            "Build" : "stocky",
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
            "Region" : random.choice((
                "North Africa",
                "East Africa",
                "southern Africa",
            ))
        }
    },
    'Caribbean' : {
        "Eyes" : random.choice((eye_color[0], eye_color[1],eye_color[3])),
        "Hair" : random.choice((hair_color[1],hair_color[2],hair_color[7])),
        "skin_tone" : random.choice((skin_tone[10], skin_tone[4],skin_tone[3],skin_tone[5]))
    },
    'Latino/Hispanic' : {
        "Eyes" : random.choice((eye_color[0], eye_color[2], eye_color[3])), 
        "Hair" : random.choice((hair_color[1],hair_color[2],hair_color[7])),
        "skin_tone" : random.choice((skin_tone[10], skin_tone[4], skin_tone[3],skin_tone[5], skin_tone[10]))
    },
    'Caucasian' : {
        "Eyes" : random.choice((eye_color[0], eye_color[2], eye_color[3])),
        "Hair" : hair_color,
        "skin_tone" : random.choice((skin_tone[9], skin_tone[9],skin_tone[8],skin_tone[7],skin_tone[2]))
    },
    'South_Asian' : {
        "Eyes" : random.choice((eye_color[0], eye_color[1])),
        "Hair" : random.choice((hair_color[1],hair_color[2],hair_color[7])),
        "skin_tone" : random.choice((skin_tone[10], skin_tone[8],skin_tone[1]))
    },
    'East_Asian' : {
        "Eyes" : random.choice((eye_color[0], eye_color[1])),
        "Hair" : random.choice((hair_color[10], hair_color[2],hair_color[7], hair_color[11])),
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
        "Eyes" : (eye_color),
        "Hair" : random.choice((hair_color[1],hair_color[2],hair_color[7],hair_color[3],hair_color[9])),
        "skin_tone" : random.choice((skin_tone[9], skin_tone[6], skin_tone[7] ,skin_tone[2], skin_tone[2], skin_tone[8], skin_tone[3]))
    }}
}

# Kapoidni - Capoid
# krovaci
# O Khoisanech se ve své knize O původu člověka z roku 1871 zmiňoval i Charles Darwin, kdy komentoval výraznou steatopygii a prodloužené malé stydké pysky u žen.[8] Od okolních bantuských populací se rovněž liší přítomností epikantu. Tyto typické a výrazné fyziologické rysy vedly ve 20. století C. S. Coona k popisu Khoisanů jako samostatné lidské rasy (kapoidní rasy),[9][10] přestože snaha klasifikovat lidstvo do ras je dnes mnohdy považována za překonanou.[11][12] Geneticky jsou Khoisany velmi starobylou monofyletickou skupinou, od které se odštěpil a později vyvinul celý zbytek lidstva.[13] Haploskupina L0, která je typická pro mitochondriální genom Khoisanů, je první odnoží mitochondriální Evy. Její odštěpení datujeme do doby před 170 000 až 150 000 lety.

# Australci:
# výrazný nadočnicový oblouk,
# absence nosního prahu a jamky, široký a kruhovitý nosní otvor, zvětšení lebky v oblasti horní čelisti (prognatie) a dlouhou (dolichocefalní) hlavu. Mezi další tradičně sdílené znaky patří plochý široký nos, silné terciární tělesné ochlupení, tmavě hnědé zbarvení kůže a kudrnaté vlasy.
# 
# Častým znakem australoidní rasy jsou také světlé (blond) vlasy, které se vyskytují hlavně u dětí a s přibývajícím věkem tmavnou. Jev je nápadný zvláště u Austrálců žijících ve středozápadní části Austrálie, kde má 90–100 % dětí světlé vlasy. Tato barva vlasů je způsobena mutací genu TYRP1, která se vyvinula nezávisle a je odlišná od mechanismu, jakým vznikají světlé vlasy u europoidů. Může jít o důsledek mísení s neznámým lidským předkem.[3]

if any(s in race_choice for s in ('Caribbean', 'Latino/Hispanic', 'Caucasian', 'South_Asian', 'East_Asian', 'Mixed')):
    race_chosen=race_details[race_choice]
    race_chosen_data=""
    # print("\n", race_details[race_choice].items(), "\n")
    make_list = list(Height)
    HEIGHT = random.choice(make_list)
    HEIGHT = (HEIGHT.value)
else: 
    race_chosen=random.choice(list(race_details[race_choice].items()))
    race_chosen_data=race_details[race_choice][race_chosen[0]]
    # print(random.choice(list(race_details[race_choice].items())), "\n")
