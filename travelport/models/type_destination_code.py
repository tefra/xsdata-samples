from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeDestinationCode(Enum):
    """
    List of valid Destination Codes.

    Properties
    ----------
    MEXICO_COST_RICA_CENTRAL_AMERICA
        Mexico/Central America/Canal Zone/Costa Rica
    CARIBBEAN
        Island and Countries of The Caribbean
    SOUTH_AMERICA
        South America
    EUROPE
        Europe
    AFRICA
        Africa
    MIDDLE_EAST_WESTERN_ASIA
        Middle East/Western Asia
    ASIA
        Asia
    AUSTRALIA_NEW_ZEALAND_PACIFIC_ISLANDS
        Australia/New Zealand/Pacific Islands
    CANADA_GREENLAND
        Canada and Greenland
    USA
        United States of America
    """

    MEXICO_COST_RICA_CENTRAL_AMERICA = "MexicoCostRicaCentralAmerica"
    CARIBBEAN = "Caribbean"
    SOUTH_AMERICA = "SouthAmerica"
    EUROPE = "Europe"
    AFRICA = "Africa"
    MIDDLE_EAST_WESTERN_ASIA = "MiddleEastWesternAsia"
    ASIA = "Asia"
    AUSTRALIA_NEW_ZEALAND_PACIFIC_ISLANDS = "AustraliaNewZealandPacificIslands"
    CANADA_GREENLAND = "CanadaGreenland"
    USA = "USA"
