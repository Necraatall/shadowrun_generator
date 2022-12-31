import random

from GeneratorJmen.Data.NickName.nicknames_cz import *

nicknames = (
    intent_nickNames_cz
)


class Nickname:
    @staticmethod
    def get_random_tribe_nickname():
        return get_random_nickname()


@staticmethod
def get_random_nickname():
    return random.choice(random.choice(nicknames))
