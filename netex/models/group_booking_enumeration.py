from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GroupBookingEnumeration(Enum):
    GROUPS_ALLOWED = "groupsAllowed"
    GROUPS_NOT_ALLOWED = "groupsNotAllowed"
    GROUPS_ALLOWED_WITH_RESERVATION = "groupsAllowedWithReservation"
    GROUP_BOOKINGS_RESTRICTED = "groupBookingsRestricted"
    UNKNOWN = "unknown"
