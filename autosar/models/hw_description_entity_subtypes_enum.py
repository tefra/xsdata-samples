from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class HwDescriptionEntitySubtypesEnum(StrEnum):
    HW_DESCRIPTION_ENTITY = "HW-DESCRIPTION-ENTITY"
    HW_ELEMENT = "HW-ELEMENT"
    HW_PIN = "HW-PIN"
    HW_PIN_GROUP = "HW-PIN-GROUP"
    HW_TYPE = "HW-TYPE"
