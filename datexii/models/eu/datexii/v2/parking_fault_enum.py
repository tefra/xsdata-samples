from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingFaultEnum(Enum):
    """
    Types of parking site or access faults.

    :cvar COMMUNICATIONS_FAILURE: Communications failure affecting
        parking site.
    :cvar BARRIER_MALFUNCTION: The entrance or exit barrier(s) are
        malfunctioning causing access problems to vehicles.
    :cvar ENTRANCE_EXIT_OBSTRUCTED: One or more entrances or exits are
        obstructed to some degree causing access problems to vehicles.
    :cvar ERRONEOUS_OCCUPANCY_INFORMATION: Occupancy information is
        subject to errors due to malfunctioning equipment.
    :cvar ERRONEOUS_OCCUPANCY_DISPLAYED: Occupancy information displayed
        on signs associated with parking site (e.g. at entrance) are
        erroneous.
    :cvar PAYMENT_MACHINES_INOPERATIVE: Payment machines are not
        functioning normally.
    :cvar RESERVATION_SERVICE_OUT_OF_ORDER: Reservation service out of
        order.
    :cvar NO_PARKING_INFORMATION_AVAILABLE: No parking information
        available.
    :cvar UNSPECIFIED: General fault of unspecified type.
    :cvar UNKNOWN: Unknown parking facility fault.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    COMMUNICATIONS_FAILURE = "communicationsFailure"
    BARRIER_MALFUNCTION = "barrierMalfunction"
    ENTRANCE_EXIT_OBSTRUCTED = "entranceExitObstructed"
    ERRONEOUS_OCCUPANCY_INFORMATION = "erroneousOccupancyInformation"
    ERRONEOUS_OCCUPANCY_DISPLAYED = "erroneousOccupancyDisplayed"
    PAYMENT_MACHINES_INOPERATIVE = "paymentMachinesInoperative"
    RESERVATION_SERVICE_OUT_OF_ORDER = "reservationServiceOutOfOrder"
    NO_PARKING_INFORMATION_AVAILABLE = "noParkingInformationAvailable"
    UNSPECIFIED = "unspecified"
    UNKNOWN = "unknown"
    OTHER = "other"
