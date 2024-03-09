from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class GeoRestrictionEnum(Enum):
    NL = "NL"
    BENELUX = "BENELUX"
    NLBES = "NLBES"
    NLALL = "NLALL"
    EU = "EU"
    EUROPE = "EUROPE"


GeoRestrictionEnum.NL.__doc__ = "Media only playable in the Netherlands."
GeoRestrictionEnum.BENELUX.__doc__ = (
    "Media only playable in the Benelux (Belgium, Netherlands, Luxembourg). "
    "This is unused."
)
GeoRestrictionEnum.NLBES.__doc__ = "New in 5.6.  Nederland plus BES gemeentes"
GeoRestrictionEnum.NLALL.__doc__ = (
    "New in 5.6. Nederland plus BES gemeentes plus Curacao, St. Maarten en "
    "Aruba"
)
GeoRestrictionEnum.EU.__doc__ = (
    "New in 5.6. EU (incl. BES gemeentes, Curacao, St. Maarten en Aruba)"
)
GeoRestrictionEnum.EUROPE.__doc__ = (
    "New in 5.6. Europa in breedste zin van het woord"
)
