from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class OnInitiatorInitiative(StrEnum):
    REQUIRES = "requires"
    PROVIDES = "provides"
    BOTH = "both"
