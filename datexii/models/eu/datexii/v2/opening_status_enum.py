from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class OpeningStatusEnum(Enum):
    """
    The opening status of some entity (e.g. parking site, service facility,
    access,...).

    :cvar OPEN: Open resp. available.
    :cvar CLOSED: Closed, usually because of the regular opening times.
    :cvar CLOSED_ABNORMAL: Closed because of some scheduled or
        unscheduled event, like holiday, maintenance, construction works
        or any kind of problems. It is possible that the closure will
        last for some time.
    :cvar OPENING_TIMES_IN_FORCE: The normal opening times are in force,
        i.e. it is not explicit said if it's open right now.
    :cvar STATUS_UNKNOWN: The opening status is unknown.
    :cvar OTHER: Other.
    """

    OPEN = "open"
    CLOSED = "closed"
    CLOSED_ABNORMAL = "closedAbnormal"
    OPENING_TIMES_IN_FORCE = "openingTimesInForce"
    STATUS_UNKNOWN = "statusUnknown"
    OTHER = "other"
