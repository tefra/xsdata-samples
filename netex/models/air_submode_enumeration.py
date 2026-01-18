from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AirSubmodeEnumeration(Enum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    INTERNATIONAL_FLIGHT = "internationalFlight"
    DOMESTIC_FLIGHT = "domesticFlight"
    INTERCONTINENTAL_FLIGHT = "intercontinentalFlight"
    DOMESTIC_SCHEDULED_FLIGHT = "domesticScheduledFlight"
    SHUTTLE_FLIGHT = "shuttleFlight"
    INTERCONTINENTAL_CHARTER_FLIGHT = "intercontinentalCharterFlight"
    INTERNATIONAL_CHARTER_FLIGHT = "internationalCharterFlight"
    ROUND_TRIP_CHARTER_FLIGHT = "roundTripCharterFlight"
    SIGHTSEEING_FLIGHT = "sightseeingFlight"
    HELICOPTER_SERVICE = "helicopterService"
    DOMESTIC_CHARTER_FLIGHT = "domesticCharterFlight"
    SCHENGEN_AREA_FLIGHT = "SchengenAreaFlight"
    AIRSHIP_SERVICE = "airshipService"
    SHORT_HAUL_INTERNATIONAL_FLIGHT = "shortHaulInternationalFlight"
