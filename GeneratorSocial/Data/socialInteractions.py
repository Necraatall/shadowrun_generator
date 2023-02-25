import random
from enum import Enum

class Interactions(Enum):
    APATHETIC = "apathetic"
    SUBCULTURES = "subcultures orientation"
    HEAD = "own head"
    HANDS = "own hands"
    CUSTOMERS = "customers"
    GUARDING = "guarding or keeping"
    BUSINESS = "business"
    PARENTS = "parents or those who brought him up"
    YOUNGER = "younger"
    VERY_OLD = "very old people"
    EQUALLY_OLD = "equally old people"
    OLDER = "older people"
    OPPOSITE_SEX = "the opposite sex"
    RAISED_HER = "those who raised her"
    TALKING_TO_GROUP = "talking to more people"
    FRIENDS = "friends"
    ACQUAINTANCES = "acquaintances"
    NEIGHBOURS = "neighbours"
    STRANGERS = "complete strangers"
    AUTHORITY = "authority figures"
    SAINTS = "samans/priests... people who have to deal with gods"
    SCUM = "the scum"
    TRADING = "trading"
    SEX_WORKERS = "sex workers"
    GAMBLING = "gambling"
    LIGHT_DOPE = "light dope (weed, cigars)"
    PUBS = "peoples at pubs and parties"
    HIGH_SOCIETY = "high society"
    RULERS = "the rulers of large territories"
    POPES = "high church leaders/sisters..."
    MAGICIANS = "magical practitioners"
    MAGICAL_BEEINGS = "magically natural creatures"
    SPIRITS = "souls of the dead and reanimated corpses"

class Interaction_places(Enum):
    CITY = "in the city"
    NATURE = "in nature"
    COUNTRYSIDE = "in the countryside"
    WILDERNESS = "in the wilderness"
    CELLAR = "in the basement"
    ROOF = "in the attic"
    CLOSED_SPACES = "in closed spaces"
    OPEN_SPACES = "in open spaces"
    HIGH_PLACES = "in high places"

make_list = list(Interactions)
GROWN_WORK_INTERACTIONS = random.sample(make_list, 2)
GROWN_NEGATIVE_WORK_INTERACTIONS = random.sample(make_list, 2)
GROWN_WORK_INTERACTIONS = f"He's comfortable working with {GROWN_WORK_INTERACTIONS[0].value} and {GROWN_WORK_INTERACTIONS[1].value} \
    and not comfortable in working with {GROWN_NEGATIVE_WORK_INTERACTIONS[0].value} and {GROWN_NEGATIVE_WORK_INTERACTIONS[1].value}."

GROWN_TALK_INTERACTIONS = random.sample(make_list, 2)
GROWN_NEGATIVE_TALK_INTERACTIONS = random.sample(make_list, 2)
GROWN_TALK_INTERACTIONS = f"He's comfortable talking with {GROWN_TALK_INTERACTIONS[0].value} and {GROWN_TALK_INTERACTIONS[1].value} \
    and not comfortable in talking with {GROWN_NEGATIVE_TALK_INTERACTIONS[0].value} and {GROWN_NEGATIVE_TALK_INTERACTIONS[1].value}."


YOUNG_WORK_INTERACTIONS = random.sample(make_list, 2)
YOUNG_NEGATIVE_WORK_INTERACTIONS = random.sample(make_list, 2)
YOUNG_WORK_INTERACTIONS = f"He's comfortable working with {YOUNG_WORK_INTERACTIONS[0].value} and {YOUNG_WORK_INTERACTIONS[1].value} \
    and not comfortable in working with {YOUNG_NEGATIVE_WORK_INTERACTIONS[0].value} and {YOUNG_NEGATIVE_WORK_INTERACTIONS[1].value}."

YOUNG_TALK_INTERACTIONS = random.sample(make_list, 2)
YOUNG_NEGATIVE_TALK_INTERACTIONS = random.sample(make_list, 2)
YOUNG_TALK_INTERACTIONS = f"As Young he's comfortable in talking with {YOUNG_TALK_INTERACTIONS[0].value} and {YOUNG_TALK_INTERACTIONS[1].value} \
    not comfortable talking with {YOUNG_NEGATIVE_TALK_INTERACTIONS[0].value} \
    and {YOUNG_NEGATIVE_TALK_INTERACTIONS[1].value}\."


make_list = list(Interaction_places)
Grown_place_to_be = random.choice(make_list)
Grown_place_to_not_be = random.choice(make_list)
COMFORTABLE_PLACE_TO_BE = f"He's comfortable {Grown_place_to_be.value} and not comfortable {Grown_place_to_not_be.value}."

Young_place_to_be = random.choice(make_list)
Young_place_not_to_be = random.choice(make_list)
YOUNG_COMFORTABLE_PLACE_TO_BE = f"He's comfortable {Young_place_to_be.value} and not comfortable {Young_place_not_to_be}."


# TODO: jako s vlasy dodat do stringu
""" otazky a vety vystupu na ktere musi sedet stringy z ciselniku:
He's comfortable working with: 

As Young he's comfortable working with 
As Young he's not comfortable working with
As Young he's comfortable talking with
As Young he's not comfortable talking with
"""