from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TdEventSwcSubtypesEnum(Enum):
    TD_EVENT_SWC = "TD-EVENT-SWC"
    TD_EVENT_SWC_INTERNAL_BEHAVIOR = "TD-EVENT-SWC-INTERNAL-BEHAVIOR"
    TD_EVENT_SWC_INTERNAL_BEHAVIOR_REFERENCE = (
        "TD-EVENT-SWC-INTERNAL-BEHAVIOR-REFERENCE"
    )
