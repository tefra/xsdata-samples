from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingSpecialLocationEnum(Enum):
    """
    Locations, often associated with a building, for a
    SpecialLocationParkingSite.

    :cvar AIRPORT_TERMINAL: The parking site is associated with an
        airport terminal.
    :cvar EXHIBITON_CENTRE: The parking site is associated with an
        exhibition centre.
    :cvar SHOPPING_CENTRE: The parking site is associated with a
        shopping centre.
    :cvar SPECIFIC_FACILITY: The parking site is associated with a
        specific facility (e.g. a hospital, a tourist site, a garden
        centre, a park etc.).. Attribute "parkingOtherSpecialLocation"
        may be used to specify details.
    :cvar TRAIN_STATION: The parking site is associated with a train
        station.
    :cvar CAMPGROUND: The parking site is associated with a campground.
    :cvar THEME_PARK: The parking site is associated with a theme park.
    :cvar FERRY_TERMINAL: The parking site is associated with a ferry
        terminal.
    :cvar VEHICLE_ON_RAIL_TERMINAL: The parking site is associated with
        a vehicle-to-rail terminal.
    :cvar COACH_STATION: The parking site is associated with a coach
        station.
    :cvar CABLE_CAR_STATION: The parking site is associated with a cable
        car station.
    :cvar PUBLIC_TRANSPORT_STATION: The parking site is associated with
        a public transport station.
    :cvar MARKET: The parking site is associated with a market.
    :cvar RELIGIOUS_CENTRE: The parking site is associated with a
        religious centre.
    :cvar CONVENTION_CENTRE: The parking site is associated with a
        convention centre.
    :cvar CINEMA: The parking site is associated with a cinema.
    :cvar SKILIFT: The parking site is associated with a ski lift.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: The parking site is associated with some other
        location. Use "parkingOtherSpecialLocation" to specify details.
    """

    AIRPORT_TERMINAL = "airportTerminal"
    EXHIBITON_CENTRE = "exhibitonCentre"
    SHOPPING_CENTRE = "shoppingCentre"
    SPECIFIC_FACILITY = "specificFacility"
    TRAIN_STATION = "trainStation"
    CAMPGROUND = "campground"
    THEME_PARK = "themePark"
    FERRY_TERMINAL = "ferryTerminal"
    VEHICLE_ON_RAIL_TERMINAL = "vehicleOnRailTerminal"
    COACH_STATION = "coachStation"
    CABLE_CAR_STATION = "cableCarStation"
    PUBLIC_TRANSPORT_STATION = "publicTransportStation"
    MARKET = "market"
    RELIGIOUS_CENTRE = "religiousCentre"
    CONVENTION_CENTRE = "conventionCentre"
    CINEMA = "cinema"
    SKILIFT = "skilift"
    UNKNOWN = "unknown"
    OTHER = "other"
