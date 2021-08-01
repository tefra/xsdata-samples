from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ReservationTypeEnum(Enum):
    """
    Reservation type enum.

    :cvar OPTIONAL: Places can be reserved, but must not.
    :cvar MANDATORY: Places need to be reserved.
    :cvar NOT_AVAILABLE: Places cannot be reserved.
    :cvar PARTLY: Some places can or must be reserved, others not (do
        not use when specifying a single parking space).
    :cvar UNKNOWN: Possibility of reservation is unknown,
    :cvar UNSPECIFIED: Possibility of reservation is not specified.
    """
    OPTIONAL = "optional"
    MANDATORY = "mandatory"
    NOT_AVAILABLE = "notAvailable"
    PARTLY = "partly"
    UNKNOWN = "unknown"
    UNSPECIFIED = "unspecified"
