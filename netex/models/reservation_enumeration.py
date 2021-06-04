from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ReservationEnumeration(Enum):
    RESERVATIONS_COMPULSORY = "reservationsCompulsory"
    RESERVATIONS_COMPULSORY_FOR_GROUPS = "reservationsCompulsoryForGroups"
    RESERVATIONS_COMPULSORY_FOR_FIRST_CLASS = "reservationsCompulsoryForFirstClass"
    RESERVATIONS_COMPULSORY_FROM_ORIGIN_STATION = "reservationsCompulsoryFromOriginStation"
    RESERVATIONS_RECOMMENDED = "reservationsRecommended"
    RESERVATIONS_POSSIBLE = "reservationsPossible"
    RESERVATIONS_POSSIBLE_ONLY_IN_FIRST_CLASS = "reservationsPossibleOnlyInFirstClass"
    RESERVATIONS_POSSIBLE_ONLY_IN_SECOND_CLASS = "reservationsPossibleOnlyInSecondClass"
    RESERVATIONS_POSSIBLE_FOR_CERTAIN_CLASSES = "reservationsPossibleForCertainClasses"
    GROUP_BOOKING_RESTRICTED = "groupBookingRestricted"
    NO_GROUPS_ALLOWED = "noGroupsAllowed"
    NO_RESERVATIONS_POSSIBLE = "noReservationsPossible"
    WHEELCHAIR_ONLY_RESERVATIONS = "wheelchairOnlyReservations"
    BICYCLE_RESERVATIONS_COMPULSORY = "bicycleReservationsCompulsory"
    RESERVATIONS_SUPPLEMENT_CHARGED = "reservationsSupplementCharged"
    UNKNOWN = "unknown"
