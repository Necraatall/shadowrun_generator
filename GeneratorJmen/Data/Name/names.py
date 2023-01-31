import random

import names_gk as names_gk
import names_fi as names_fi
import names_pl as names_pl
import names_it as names_it
import names_no as names_no
import names_ne as names_ne
import names_se as names_se
import names_hu as names_hu
import names_us as names_us
import names_sk as names_sk
import names_fr as names_fr
import names_es as names_es
import names_vn as names_vn
import names_cz as names_cz

names_all = (
    names_gk.intent_names_gk,
    names_fi.intent_names_fi,
    names_pl.intent_names_pl,
    names_it.intent_names_it,
    names_no.intent_names_no,
    names_ne.intent_names_ne,
    names_se.intent_names_se,
    names_hu.intent_names_hu,
    names_us.intent_names_us,
    names_sk.intent_names_sk,
    names_fr.intent_names_fr,
    names_es.intent_names_es,
    names_vn.intent_names_vn
)


class Name:
    @staticmethod
    def get_random_tribe_name():
        return get_random_name()


@staticmethod
def get_random_name():
    return random.choice(random.choice(names_all))
