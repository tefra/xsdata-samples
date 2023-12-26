from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeGeoPoliticalAreaType1(Enum):
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
