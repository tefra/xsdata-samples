from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ListEnumSimple(Enum):
    """
    :cvar NUMBER: This indicates that the list is an numerated list.
    :cvar UNNUMBER: This indicates that it is an enumeration (bulleted
        list)
    """
    NUMBER = "NUMBER"
    UNNUMBER = "UNNUMBER"
