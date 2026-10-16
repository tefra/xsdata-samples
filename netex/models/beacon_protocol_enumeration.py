from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BeaconProtocolEnumeration(StrEnum):
    I_BEACON = "iBeacon"
    EDDYSTONE = "Eddystone"
    VDV431 = "VDV431"
