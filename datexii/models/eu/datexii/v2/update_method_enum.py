from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class UpdateMethodEnum(Enum):
    """
    The types of updates of situations that may be requested by a client.

    :cvar ALL_ELEMENT_UPDATE: The client has currently requested that
        all situation elements are sent when one or more component
        elements are updated.
    :cvar SINGLE_ELEMENT_UPDATE: The client has currently requested that
        only the individual elements of a situation that have changed
        are sent when updated.
    :cvar SNAPSHOT: The client has requested that all situations and
        their elements which are valid at the time of request be sent
        together, i.e. a snapshot in time of all valid situations.
    """

    ALL_ELEMENT_UPDATE = "allElementUpdate"
    SINGLE_ELEMENT_UPDATE = "singleElementUpdate"
    SNAPSHOT = "snapshot"
