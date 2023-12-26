from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class AreaOfInterestEnum(Enum):
    """
    Types of areas of interest.

    :cvar CONTINENT_WIDE: Area of the whole European continent.
    :cvar NATIONAL: Whole area of the specific country.
    :cvar NEIGHBOURING_COUNTRIES: Area of countries which are
        neighbouring the one specified.
    :cvar NOT_SPECIFIED: Non specified area.
    :cvar REGIONAL: Area of the local region.
    """

    CONTINENT_WIDE = "continentWide"
    NATIONAL = "national"
    NEIGHBOURING_COUNTRIES = "neighbouringCountries"
    NOT_SPECIFIED = "notSpecified"
    REGIONAL = "regional"
