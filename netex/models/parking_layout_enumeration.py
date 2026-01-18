from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingLayoutEnumeration(Enum):
    COVERED = "covered"
    OPEN_SPACE = "openSpace"
    MULTISTOREY = "multistorey"
    UNDERGROUND = "underground"
    ROADSIDE = "roadside"
    UNDEFINED = "undefined"
    OTHER = "other"
    ON_PAVEMENT = "onPavement"
    CYCLE_HIRE = "cycleHire"
