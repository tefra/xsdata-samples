from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class XmlSpaceEnumSimple(Enum):
    """
    :cvar DEFAULT: The value "default" signals that applications'
        default white-space processing modes are acceptable for this
        element.
    :cvar PRESERVE: the value "preserve" indicates the intent that
        applications preserve all the white space.
    """

    DEFAULT = "default"
    PRESERVE = "preserve"
