from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SystemOfUnits(Enum):
    SI_METRES = "SiMetres"
    SI_KILOMETRES_AND_METRES = "SiKilometresAndMetres"
    OTHER = "Other"
