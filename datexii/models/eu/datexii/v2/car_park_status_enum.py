from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class CarParkStatusEnum(Enum):
    """
    Collection of statuses which may be associated with car parks.

    :cvar CAR_PARK_CLOSED: The specified car park is closed.
    :cvar ALL_CAR_PARKS_FULL: All car parks are full within a specified
        area.
    :cvar CAR_PARK_FACILITY_FAULTY: The specified car parking facility
        is not operating normally.
    :cvar CAR_PARK_FULL: A specified car park is completely occupied.
    :cvar CAR_PARK_STATUS_UNKNOWN: The status of the specified car
        park(s) is unknown.
    :cvar ENOUGH_SPACES_AVAILABLE: Specified car parks have car-parking
        spaces available.
    :cvar MULTI_STORY_CAR_PARKS_FULL: Multi level car parks are fully
        occupied.
    :cvar NO_MORE_PARKING_SPACES_AVAILABLE: Specified car parks are
        fully occupied.
    :cvar NO_PARK_AND_RIDE_INFORMATION: No park and ride information
        will be available until the specified time.
    :cvar NO_PARKING_ALLOWED: No parking allowed until the specified
        time.
    :cvar NO_PARKING_INFORMATION_AVAILABLE: Car-parking information is
        not available until a specified time.
    :cvar NORMAL_PARKING_RESTRICTIONS_LIFTED: The parking restrictions
        that normally apply in the specified location have been
        temporarily lifted.
    :cvar ONLY_AFEW_SPACES_AVAILABLE: Specified car parks have 95% or
        greater occupancy.
    :cvar PARK_AND_RIDE_SERVICE_NOT_OPERATING: Park and ride services
        are not operating until the specified time.
    :cvar PARK_AND_RIDE_SERVICE_OPERATING: Park and ride services are
        operating until the specified time.
    :cvar SPECIAL_PARKING_RESTRICTIONS_IN_FORCE: Parking restrictions,
        other than those that normally apply, are in force in a
        specified area.
    """
    CAR_PARK_CLOSED = "carParkClosed"
    ALL_CAR_PARKS_FULL = "allCarParksFull"
    CAR_PARK_FACILITY_FAULTY = "carParkFacilityFaulty"
    CAR_PARK_FULL = "carParkFull"
    CAR_PARK_STATUS_UNKNOWN = "carParkStatusUnknown"
    ENOUGH_SPACES_AVAILABLE = "enoughSpacesAvailable"
    MULTI_STORY_CAR_PARKS_FULL = "multiStoryCarParksFull"
    NO_MORE_PARKING_SPACES_AVAILABLE = "noMoreParkingSpacesAvailable"
    NO_PARK_AND_RIDE_INFORMATION = "noParkAndRideInformation"
    NO_PARKING_ALLOWED = "noParkingAllowed"
    NO_PARKING_INFORMATION_AVAILABLE = "noParkingInformationAvailable"
    NORMAL_PARKING_RESTRICTIONS_LIFTED = "normalParkingRestrictionsLifted"
    ONLY_AFEW_SPACES_AVAILABLE = "onlyAFewSpacesAvailable"
    PARK_AND_RIDE_SERVICE_NOT_OPERATING = "parkAndRideServiceNotOperating"
    PARK_AND_RIDE_SERVICE_OPERATING = "parkAndRideServiceOperating"
    SPECIAL_PARKING_RESTRICTIONS_IN_FORCE = "specialParkingRestrictionsInForce"
