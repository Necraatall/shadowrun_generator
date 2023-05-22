from enum import Enum
import random
from .Data.race_details import *


race_choice = random.choice(('Europoidic', 'Caucasian', 'Latino/Hispanic', 'African', 'Caribbean', 'Middle_Eastern', 'South_Asian', 'East_Asian', 'Mixed'))
if race_choice == 'Europoidic':
    sub_race_europoidic_choice = random.choice(('Nordic', 'Falian', 'Baltic', 'Mediterran', 'Dinaric', 'Alpine'))
if race_choice == 'Middle_Eastern':
    sub_race_middle_eastern_choices = random.choice(('Hamitic', 'Sudeten', 'Oriental'))
if race_choice == 'African':
    sub_race_african_choice = random.choice(('Hamitic'))


race_chosen = random.choice(list(race_details[race_choice].items()))

if race_choice == 'Europoidic':
    race = random.choice(list(race_details[race_choice]))
    race_chosen = race

race_chosen_height = ('Falian', 'Hamitic', 'Sudeten', 'Oriental', 'Alpine', 'Mediterran')

make_list = list(Face_shape)
if any(s in race_choice for s in race_chosen_height):
    make_list = list(Height)
    HEIGHT = random.choice(make_list)
    HEIGHT = (HEIGHT.value)

    if race_chosen == 'Hamitic' or race_chosen == 'Alpine':
        face_shape = "Round"

    if race_chosen == 'Mediterran':
        face_shape = "Oval"

    if race_chosen == 'Falian':
        face_shape = "Square"

    if not any(s in race_chosen for s in ('Hamitic', 'Alpine', 'Mediterran', 'Falian')):
        face_shape = random.choice(make_list)
        face_shape = (face_shape.value)

else:
    face_shape = random.choice(make_list)
    face_shape = (face_shape.value)

FACE_SHAPE = face_shape
