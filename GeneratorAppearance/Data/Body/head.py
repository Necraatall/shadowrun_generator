from enum import Enum
import random
from ..Body.body import *

class Face_shape(Enum):
    OVAL_FACE_SHAPE = "Oval" 
    SQUARE_FACE_SHAPE = "Square"
    OBLONG_FACE_SHAPE = "Oblong"
    TRIANGULAR_FACE_SHAPE = "Triangular"
    ROUND_FACE_SHAPE = "Round"
    DIAMOND_FACE_SHAPE = "Diamond"
    HEART_FACE_SHAPE = "Heart"

make_list = list(Face_shape)
if not any(s in race_choice for s in ('Caribbean', 'Latino/Hispanic', 'Caucasian', 'South_Asian', 'East_Asian', 'Mixed')):
    if race_chosen[0]=='Hamitic' :
        face_shape = "Round"

    if race_chosen[0]=='Alpine':
        face_shape = "Round"

    if race_chosen[0]=='Mediterran':
        face_shape = "Oval"

    if race_chosen[0]=='Falian':
        face_shape = "Square"
    
    if not any(s in race_choice for s in ('Hamitic', 'Alpine', 'Mediterran', 'Falian')):
        face_shape = random.choice(make_list)
        face_shape = (face_shape.value)

else: 
    face_shape = random.choice(make_list)
    face_shape = (face_shape.value)
FACE_SHAPE = face_shape

class Long_hair_styles(Enum):
    SHAG_HAIRCUT = "shag haircut"
    LONG_CURLY_HAIR = "long curly hair"
    LONG_LAYERED = "long layered"
    LONG_HAIRSTYLE_WITH_TEXTURE_WAVES = "long hairstyle with texture waves"
    LONG_STRAIGHT_HAIR = "long straight hair"
    LONG_HAIRSTYLE_WITH_SIDE_PART = "long hairstyle with side part"
    LONG_HAIR_WITH_MIDDLE_PART = "long hair with middle part"
    LONG_SURFER_HAIR = "long surfer hair"
    LONG_DREADLOCKS = "long dreadlocks"
    MAN_BUN = "man bun"
    MAN_BUN_WITH_FADE = "man bun with fade"
    LONG_HAIRSTYLE_WITH_QUIFF = "long hairstyle with quiff"
    BRAIDS_FOR_MAN = "braids for man"
    LONG_HALF_UP = "long half up"
    LONG_VIKING = "long viking"
    PONYTAIL = "ponytail"
    PONYTAIL_WITH_UNDERCUT = "ponytail with undercut"
    LONG_SLICK_BACK = "long slick back"
    BRO_FLOW = "bro flow"
    LONG_HAIR_WITH_BANGS = "long hair with bangs"
    SHOULDER_LENGTH_LONG_HAIR = "shoulder length long hair"
    LONG_TIGHT_CURLS = "long tight curls"
    LONG_HAIRSTYLE_WITH_FRINGE = "long hairstyle with fringe"
    LONG_HAIR_DYED_HAIR = "long hair dyed hair"
    MULLET_HAIRCUT = "mullet haircut"
    LONG_HAIR_WITH_FADE = "long hair with fade"
    LONG_HAIR_WITH_UNDERCUT = "long hair with undercut"
    LONG_HAIRSTYLES_FOR_MEN_WITH_THICK_HAIR = "long hairstyles for men with thick hair"
    LONG_HAIR_WITH_POMPADOUR = "long hair with pompadour"
    LONG_HAIR_HARD_PART = "long hair hard part"

make_list = list(Long_hair_styles)
LONG_HAIR_STYLES = random.choice(make_list)
LONG_HAIR_STYLES = (LONG_HAIR_STYLES.value)

class Oval_short_hair_styles(Enum):
    PUSHED_BACK_LONG_OVAL_HAIR_STYLE_SHORT = "pushed back long"
    SIDE_PARTED_SHORT_OVAL_HAIR_STYLE_SHORT = "side parted short"
    UNDERCUT_OVAL_HAIR_STYLE_SHORT = "undercut"
    FRINGE_UP_OVAL_HAIR_STYLE_SHORT = "fringe up"

make_list = list(Oval_short_hair_styles)
OVAL_SHORT_HAIR_STYLES = random.choice(make_list)
OVAL_SHORT_HAIR_STYLES = (OVAL_SHORT_HAIR_STYLES.value)

class Square_short_hair_styles(Enum):
    CREW_AKA_BUZZ_CUT_SQUARE_HAIR_STYLE_SHORT = "crew aka buzz cut"
    UNDERCUT_SQUARE_HAIR_STYLE_SHORT = "undercut"
    FAUX_HAWK_SQUARE_HAIR_STYLE_SHORT = "faux hawk"
    SLICKED_BACK_SIDE_PART_SQUARE_HAIR_STYLE_SHORT = "slicked back side part"

make_list = list(Square_short_hair_styles)
SQUARE_SHORT_HAIR_STYLES = random.choice(make_list)
SQUARE_SHORT_HAIR_STYLES = (SQUARE_SHORT_HAIR_STYLES.value)

class Oblong_short_hair_styles(Enum):
    SIDE_PARTED_OBLONG_HAIR_STYLE_SHORT = "side parted"
    BUZZ_CUT_OBLONG_HAIR_STYLE_SHORT = "buz cut"
    FRINGE_UP_OBLONG_HAIR_STYLE_SHORT = "fringe up"
    SIDE_FRINGE_OBLONG_HAIR_STYLE_SHORT = "side fringe"

class Triangular_short_hair_styles(Enum):
    FRINGE_UP_TRIANGULAR_HAIR_STYLE_SHORT = "fringe up"
    SIDE_FRINGE_TRIANGULAR_HAIR_STYLE_SHORT = "side fringe"
    SIDE_PARTED_TRIANGULAR_HAIR_STYLE_SHORT = "side parted"

class Round_short_hair_styles(Enum):
    FAUX_HAWK_WITH_SHORTER_SIDES_ROUND_HAIR_STYLE_SHORT = "faux hawk with shorter sides"
    FRINGE_UP_ROUND_HAIR_STYLE_SHORT = "fringe up"
    UNDERCUT_ROUND_HAIR_STYLE_SHORT = "undercut"
    QUIFF_ROUND_HAIR_STYLE_SHORT = "quiff"

class Diamond_short_hair_styles(Enum):
    QUIFF_DIAMOND_HAIR_STYLE_SHORT = "quiff"
    LONG_HAIR_PUSHED_BACK_DIAMOND_HAIR_STYLE_SHORT = "long hair pushed back"
    FAUX_HAWK_DIAMOND_HAIR_STYLE_SHORT = "faux hawk"
    SIDE_FRINGE_DIAMOND_HAIR_STYLE_SHORT = "side fringe"

class Heart_short_hair_styles(Enum):
    LONG_FRINGES_HEART_HAIR_STYLE_SHORT = "long fringes"
    SIDE_PARTED_LONG_HEART_HAIR_STYLE_SHORT = "side parted long"
    PUSHED_BACK_HEART_HAIR_STYLE_SHORT = "pushed back"
    UNDERCUT_HEART_HAIR_STYLE_SHORT = "undercut"



class Hair_color(Enum):
    AUBURN_HAIR_COLOR = 'auburn'
    BROWN_HAIR_COLOR = 'brown'
    BLACK_HAIR_COLOR = 'black'
    BLONDE_HAIR_COLOR = 'blonde'
    COPPER_HAIR_COLOR = 'copper'
    GINGER_HAIR_COLOR = 'ginger'
    GOLDEN_HAIR_COLOR = 'golden'
    GREY_HAIR_COLOR = 'grey'
    MOUSE_HAIR_COLOR = 'mouse'
    RED_HAIR_COLOR = 'red'
    DARK_BROWN_HAIR_COLOR = 'dark brown'
    WHITE_HAIR_COLOR = 'white'

make_list = list(Hair_color)
HAIR_COLOR = random.choice(make_list)
HAIR_COLOR = (HAIR_COLOR.value)

class Hair_types(Enum):
    VERY_STRAIGHT_HAIR_TYPE = "very straight hair"
    STRAIGHT_BEND_HAIR_TYPE = "straight hair with some bends"
    STRAIGHT_COARSER_HAIR_TYPE = "straight hair with coarser texture"
    STRAIGHT_HAIR_TYPE = "straight hair"
    SOFT_WAVE_HAIR_TYPE = "soft wave"
    WAVY_HAIR_TYPE = "wavy"
    DEEP_WAVE_HAIR_TYPE = "deep wave"
    LOST_CURLS_HAIR_TYPE = "lost curls"
    SOFT_CURL_HAIR_TYPE = "soft curl"
    CURLY_HAIR_TYPE = "curly"
    ULTRA_CURLY_HAIR_TYPE = "ultra curly"
    COILED_HAIR_TYPE = "coiled"
    ZIG_ZAG_HAIR_TYPE = "zig zag"
    TIGHTLY_COILED_HAIR_TYPE = "tightly coiled"

make_list = list(Hair_types)
HAIR_TYPES = random.choice(make_list)
HAIR_TYPES = (HAIR_TYPES.value)

@staticmethod
def haircut_by_face_shape():
    match FACE_SHAPE:
        case "Oval":
            make_list = list(Oval_short_hair_styles)
            haircut = random.choice(make_list)
            haircut = haircut.value
        case "Square":
            make_list = list(Square_short_hair_styles)
            haircut = random.choice(make_list)
            haircut = haircut.value
        case "Oblong":
            make_list = list(Oblong_short_hair_styles)
            haircut = random.choice(make_list)
            haircut = haircut.value
        case "Triangular":
            make_list = list(Triangular_short_hair_styles)
            haircut = random.choice(make_list)
            haircut = haircut.value
        case "Round":
            make_list = list(Round_short_hair_styles)
            haircut = random.choice(make_list)
            haircut = haircut.value
        case "Diamond":
            make_list = list(Diamond_short_hair_styles)
            haircut = random.choice(make_list)
            haircut = haircut.value
        case "Heart":
            make_list = list(Heart_short_hair_styles)
            haircut = random.choice(make_list)
            haircut = haircut.value
    return haircut


class Face_and_hair(Enum):
    FACE_LONG = f"{FACE_SHAPE} face with naturally {HAIR_TYPES} hair of the {HAIR_COLOR} color and long haircut: {LONG_HAIR_STYLES}"
    FACE_SHORT = f"{FACE_SHAPE} face with naturally {HAIR_TYPES} hair of the {HAIR_COLOR} color and short haircut: {haircut_by_face_shape()}"

make_list = list(Face_and_hair)
FACE_AND_HAIR = random.choice(make_list)
FACE_AND_HAIR = (FACE_AND_HAIR.value)
