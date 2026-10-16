from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class ComponentPortDirectionType(StrEnum):
    """
    The direction of a component port.
    """

    IN = "in"
    OUT = "out"
    INOUT = "inout"
    PHANTOM = "phantom"
