from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class ContentRatingType(Enum):
    DISCRIMINATIE = "DISCRIMINATIE"
    GROF_TAALGEBRUIK = "GROF_TAALGEBRUIK"
    ANGST = "ANGST"
    GEWELD = "GEWELD"
    SEKS = "SEKS"
    DRUGS_EN_ALCOHOL = "DRUGS_EN_ALCOHOL"


ContentRatingType.DISCRIMINATIE.__doc__ = (
    "Discrimination. Contains depictions, or material which may encourage, "
    "discrimination."
)
ContentRatingType.GROF_TAALGEBRUIK.__doc__ = "Coarse language."
ContentRatingType.ANGST.__doc__ = (
    "Fear. May be frightening or scary for young children."
)
ContentRatingType.GEWELD.__doc__ = "Violence. Contains depictions of violence."
ContentRatingType.SEKS.__doc__ = (
    "Sex. Contains nudity and/or sexual behavior or sexual references."
)
ContentRatingType.DRUGS_EN_ALCOHOL.__doc__ = (
    "Drugs. Refers to or depicts the use of drugs."
)
