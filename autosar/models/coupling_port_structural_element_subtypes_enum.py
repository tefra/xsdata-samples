from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CouplingPortStructuralElementSubtypesEnum(Enum):
    COUPLING_PORT_FIFO = "COUPLING-PORT-FIFO"
    COUPLING_PORT_SCHEDULER = "COUPLING-PORT-SCHEDULER"
    COUPLING_PORT_SHAPER = "COUPLING-PORT-SHAPER"
    COUPLING_PORT_STRUCTURAL_ELEMENT = "COUPLING-PORT-STRUCTURAL-ELEMENT"
