from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BusSubmodeEnumeration(Enum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    LOCAL_BUS = "localBus"
    REGIONAL_BUS = "regionalBus"
    EXPRESS_BUS = "expressBus"
    NIGHT_BUS = "nightBus"
    POST_BUS = "postBus"
    SPECIAL_NEEDS_BUS = "specialNeedsBus"
    MOBILITY_BUS = "mobilityBus"
    MOBILITY_BUS_FOR_REGISTERED_DISABLED = "mobilityBusForRegisteredDisabled"
    SIGHTSEEING_BUS = "sightseeingBus"
    SHUTTLE_BUS = "shuttleBus"
    HIGH_FREQUENCY_BUS = "highFrequencyBus"
    DEDICATED_LANE_BUS = "dedicatedLaneBus"
    SCHOOL_BUS = "schoolBus"
    SCHOOL_AND_PUBLIC_SERVICE_BUS = "schoolAndPublicServiceBus"
    RAIL_REPLACEMENT_BUS = "railReplacementBus"
    DEMAND_AND_RESPONSE_BUS = "demandAndResponseBus"
    AIRPORT_LINK_BUS = "airportLinkBus"
