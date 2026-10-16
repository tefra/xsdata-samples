from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeGeoPoliticalAreaType2(StrEnum):
    """
    The type of the geographical location.
    """

    WORLD = "World"
    GLOBAL_AREA = "Global Area"
    CONTINENT_GROUP = "Continent Group"
    CONTINENT = "Continent"
    COUNTRY = "Country"
    STATE_PROVINCE = "State/Province"
    CITY = "City"
    AIRPORT = "Airport"
