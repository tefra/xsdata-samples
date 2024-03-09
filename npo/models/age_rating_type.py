from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class AgeRatingType(Enum):
    VALUE_6 = "6"
    VALUE_9 = "9"
    VALUE_12 = "12"
    VALUE_14 = "14"
    VALUE_16 = "16"
    VALUE_18 = "18"
    ALL = "ALL"
    NOT_YET_RATED = "NOT_YET_RATED"


AgeRatingType.VALUE_6.__doc__ = "Suitable for people of age 6 and up."
AgeRatingType.VALUE_9.__doc__ = "Suitable for people of age 9 and up."
AgeRatingType.VALUE_12.__doc__ = "Suitable for people of age 12 and up."
AgeRatingType.VALUE_14.__doc__ = "Suitable for people of age 12 and up."
AgeRatingType.VALUE_16.__doc__ = "Suitable for people of age 16 and up."
AgeRatingType.VALUE_18.__doc__ = "Suitable for people of age 18 and up."
AgeRatingType.ALL.__doc__ = "Suitable for people of all ages."
AgeRatingType.NOT_YET_RATED.__doc__ = "Not yet rated"
