from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SoftwarePackageActionTypeEnumSimple(Enum):
    INSTALL = "INSTALL"
    REMOVE = "REMOVE"
    UPDATE = "UPDATE"
