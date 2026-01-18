from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class FieldAccessEnumSimple(Enum):
    """
    :cvar GETTER: Access to the getter of the Field.
    :cvar GETTER_SETTER: Access to getter and setter of the field
    :cvar SETTER: Access to the setter of the Field.
    """

    GETTER = "GETTER"
    GETTER_SETTER = "GETTER-SETTER"
    SETTER = "SETTER"
