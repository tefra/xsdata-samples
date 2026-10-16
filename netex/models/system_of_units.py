from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SystemOfUnits(StrEnum):
    SI_METRES = "SiMetres"
    SI_KILOMETRES_AND_METRES = "SiKilometresAndMetres"
    OTHER = "Other"
