from enum import Enum


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

class Body(Enum):
    VERY_WELL_BUILT_BODY = "very well-built"
    WELL_BUILD_BODY = "well-built"
    AVERAGE_BUILD_BODY = "average build"
    FINE_BUILD_BODY = "fine build"
    VERY_FINE_BUILD_BODY = "very fine build"
    SKINNY_BUILD_BODY = "skinny build"
    SLENDER_BUILD_BODY = "slender build"

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
