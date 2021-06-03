from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class PersistencyRedundancyEnumSimple(Enum):
    """
    :cvar NONE_VALUE: This value represents the requirement that
        redundancy measures are not applied on persistency storage
        level.
    :cvar REDUNDANT: This value represents the requirement that
        redundancy measures are applied on persistency storage level.
        The nature of the redundant persistent storage is not further
        qualified and subject to integrator decisions.
    :cvar REDUNDANT_PER_ELEMENT: This value represents the requirement
        that redundancy measures are applied on key-value level of a
        key-value storage or on file level of a file storage.  The
        nature of the redundancy used on the persistent storage is not
        further qualified and subject to integrator decisions.
    """
    NONE_VALUE = "NONE"
    REDUNDANT = "REDUNDANT"
    REDUNDANT_PER_ELEMENT = "REDUNDANT-PER-ELEMENT"
