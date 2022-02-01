import random

Names = [
    'baggy',
    'beady',
]

Surnames = [
    'abyssinian',
    'affenpinscher'
]


def gen(repeatParts=False, separator='-', lists=(Names, Surnames)):
    name = []
    for word in lists:
        part = None
        while not part or (part in name and not repeatParts):
            part = random.choice(word)
        name.append(part)
    return separator.join(name)


print(gen(separator=" "))