from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TrafficTypeEnum(Enum):
    """
    Types of traffic, mostly classified by its destination type.

    :cvar ACCESS_ONLY_TRAFFIC: Traffic destined for local access only.
    :cvar DESTINED_FOR_AIRPORT: Traffic destined for the airport.
    :cvar DESTINED_FOR_AIRPORT_ARRIVALS: Traffic destined for airport
        arrivals.
    :cvar DESTINED_FOR_AIRPORT_DEPARTURES: Traffic destined for airport
        departures.
    :cvar DESTINED_FOR_FERRY_SERVICE: Traffic destined for the ferry
        service.
    :cvar DESTINED_FOR_RAIL_SERVICE: Traffic destined for the rail
        service.
    :cvar HOLIDAY_TRAFFIC: Traffic heading towards holiday destinations.
    :cvar LOCAL_TRAFFIC: Traffic heading towards local destinations.
    :cvar LONG_DISTANCE_TRAFFIC: Traffic heading towards destinations
        which are a long distance away.
    :cvar REGIONAL_TRAFFIC: Traffic heading towards local regional
        destinations.
    :cvar RESIDENTS_ONLY_TRAFFIC: Local residents only traffic.
    :cvar THROUGH_TRAFFIC: Traffic which is not for local access, i.e.
        traffic not destined for local town, city or built up area but
        for transit though the area.
    :cvar VISITOR_TRAFFIC: Traffic heading towards local visitor
        attraction.
    """

    ACCESS_ONLY_TRAFFIC = "accessOnlyTraffic"
    DESTINED_FOR_AIRPORT = "destinedForAirport"
    DESTINED_FOR_AIRPORT_ARRIVALS = "destinedForAirportArrivals"
    DESTINED_FOR_AIRPORT_DEPARTURES = "destinedForAirportDepartures"
    DESTINED_FOR_FERRY_SERVICE = "destinedForFerryService"
    DESTINED_FOR_RAIL_SERVICE = "destinedForRailService"
    HOLIDAY_TRAFFIC = "holidayTraffic"
    LOCAL_TRAFFIC = "localTraffic"
    LONG_DISTANCE_TRAFFIC = "longDistanceTraffic"
    REGIONAL_TRAFFIC = "regionalTraffic"
    RESIDENTS_ONLY_TRAFFIC = "residentsOnlyTraffic"
    THROUGH_TRAFFIC = "throughTraffic"
    VISITOR_TRAFFIC = "visitorTraffic"
