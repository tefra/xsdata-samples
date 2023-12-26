from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class OwnershipTypeEnum(Enum):
    """
    Ownership type enum.

    :cvar PUBLIC: Public ownership.
    :cvar PRIVATE: Private ownership.
    :cvar PUBLIC_PRIVATE: A public private partnership model.
    :cvar RESIDENT: A private individual ownership.
    :cvar UNKNOWN: An unknown kind of ownership.
    :cvar OTHER: Other kind of ownership.
    """

    PUBLIC = "public"
    PRIVATE = "private"
    PUBLIC_PRIVATE = "publicPrivate"
    RESIDENT = "resident"
    UNKNOWN = "unknown"
    OTHER = "other"
