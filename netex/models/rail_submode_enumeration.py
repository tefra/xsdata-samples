from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RailSubmodeEnumeration(Enum):
    UNKNOWN = "unknown"
    LOCAL = "local"
    HIGH_SPEED_RAIL = "highSpeedRail"
    SUBURBAN_RAILWAY = "suburbanRailway"
    REGIONAL_RAIL = "regionalRail"
    INTERREGIONAL_RAIL = "interregionalRail"
    LONG_DISTANCE = "longDistance"
    INTERNATIONAL = "international"
    SLEEPER_RAIL_SERVICE = "sleeperRailService"
    NIGHT_RAIL = "nightRail"
    CAR_TRANSPORT_RAIL_SERVICE = "carTransportRailService"
    TOURIST_RAILWAY = "touristRailway"
    AIRPORT_LINK_RAIL = "airportLinkRail"
    RAIL_SHUTTLE = "railShuttle"
    REPLACEMENT_RAIL_SERVICE = "replacementRailService"
    SPECIAL_TRAIN = "specialTrain"
    CROSS_COUNTRY_RAIL = "crossCountryRail"
    RACK_AND_PINION_RAILWAY = "rackAndPinionRailway"
