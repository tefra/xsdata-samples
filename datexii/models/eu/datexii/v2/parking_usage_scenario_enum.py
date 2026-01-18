from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingUsageScenarioEnum(Enum):
    """
    Types of parking usage (park &amp; ride, kiss &amp; ride, ...).

    :cvar TRUCK_PARKING: The parking site is designed for lorries (other
        vehicles are allowed as well).
    :cvar PARK_AND_RIDE: Parking for public transport users.
    :cvar PARK_AND_CYCLE: A parking site for people who continue their
        journey by bike.
    :cvar PARK_AND_WALK: A parking site for people who continue to walk.
    :cvar KISS_AND_RIDE: Parking site with possibility for very short
        parking to drop off (or drop on) passengers for public
        transport.
    :cvar LIFTSHARE: A parking site for people who are sharing their
        cars.
    :cvar CAR_SHARING: A parking site for people who are sharing cars
        organised by a car sharing company..
    :cvar REST_AREA: The parking site is associated with a rest area,
        i.e. people can relax some time outside their car there. Note
        that the presence of some bench, picnic place or toilet is
        already sufficient; there is no need for a restaurant or a
        building.
    :cvar SERVICE_AREA: The parking site is associated with a service
        area.
    :cvar DROP_OFF_WITH_VALET: A valet drop off service.
    :cvar DROP_OFF_MECHANICAL: A mechanical drop off service.
    :cvar EVENT_PARKING: Parking is associated with an event. Use
        'eventParkingType' or 'eventParkingType2' to specify the event.
    :cvar AUTOMATIC_PARKING_GUIDANCE: Specifies, if there is a (visual)
        guidance system within the parking site, which helps the drivers
        to find free spaces. Note: This is not a parking VMS or a
        parking route, which are usually located outside the parking
        site.
    :cvar STAFF_GUIDES_TO_SPACE: Staff guides to space.
    :cvar VEHICLE_LIFT: Vehicle lift
    :cvar LOADING_BAY: The parking site or space(s) are designed as a
        loading bay.
    :cvar DROP_OFF: The parking site or space(s) are designed for drop
        off only.
    :cvar OVERNIGHT_PARKING: The parking site or space(s) are designed
        for overnight parking. Note that the absence of this scenario
        does not automatically mean a prohibition of overnight parking.
        See also PermitsAndProhibitions.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Some other usage scenario.
    """

    TRUCK_PARKING = "truckParking"
    PARK_AND_RIDE = "parkAndRide"
    PARK_AND_CYCLE = "parkAndCycle"
    PARK_AND_WALK = "parkAndWalk"
    KISS_AND_RIDE = "kissAndRide"
    LIFTSHARE = "liftshare"
    CAR_SHARING = "carSharing"
    REST_AREA = "restArea"
    SERVICE_AREA = "serviceArea"
    DROP_OFF_WITH_VALET = "dropOffWithValet"
    DROP_OFF_MECHANICAL = "dropOffMechanical"
    EVENT_PARKING = "eventParking"
    AUTOMATIC_PARKING_GUIDANCE = "automaticParkingGuidance"
    STAFF_GUIDES_TO_SPACE = "staffGuidesToSpace"
    VEHICLE_LIFT = "vehicleLift"
    LOADING_BAY = "loadingBay"
    DROP_OFF = "dropOff"
    OVERNIGHT_PARKING = "overnightParking"
    UNKNOWN = "unknown"
    OTHER = "other"
