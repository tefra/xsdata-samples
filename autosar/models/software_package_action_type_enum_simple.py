from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SoftwarePackageActionTypeEnumSimple(StrEnum):
    INSTALL = "INSTALL"
    REMOVE = "REMOVE"
    UPDATE = "UPDATE"
