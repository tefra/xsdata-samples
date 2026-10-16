from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class DelayValueUnitType(StrEnum):
    """
    Indicates legal units for delay values.
    """

    PS = "ps"
    NS = "ns"
