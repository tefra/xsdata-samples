from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TopographicPlaceTypeEnumeration(StrEnum):
    CONTINENT = "continent"
    INTERREGION = "interregion"
    COUNTRY = "country"
    PRINCIPALITY = "principality"
    STATE = "state"
    PROVINCE = "province"
    REGION = "region"
    COUNTY = "county"
    AREA = "area"
    CONURBATION = "conurbation"
    CITY = "city"
    MUNICIPALITY = "municipality"
    QUARTER = "quarter"
    SUBURB = "suburb"
    TOWN = "town"
    URBAN_CENTRE = "urbanCentre"
    DISTRICT = "district"
    PARISH = "parish"
    VILLAGE = "village"
    HAMLET = "hamlet"
    PLACE_OF_INTEREST = "placeOfInterest"
    OTHER = "other"
    UNRECORDED = "unrecorded"
