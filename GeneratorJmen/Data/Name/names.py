import random

from ..Name.names_gk import *
from ..Name.names_fi import *
from ..Name.names_pl import *
from ..Name.names_it import *
from ..Name.names_no import *
from ..Name.names_ne import *
from ..Name.names_se import *
from ..Name.names_hu import *
from ..Name.names_us import *
from ..Name.names_sk import *
from ..Name.names_fr import *
from ..Name.names_es import *
from ..Name.names_vn import *
from ..Name.names_cz import *

names_all = (
    intent_names_gk,
    intent_names_fi,
    intent_names_pl,
    intent_names_it,
    intent_names_no,
    intent_names_ne,
    intent_names_se,
    intent_names_hu,
    intent_names_us,
    intent_names_sk,
    intent_names_fr,
    intent_names_es,
    intent_names_vn
)


class Name:
    @staticmethod
    def get_random_tribe_name():
        return get_random_name()


@staticmethod
def get_random_name():
    return random.choice(random.choice(names_all))
