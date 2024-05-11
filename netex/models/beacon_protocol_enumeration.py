from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BeaconProtocolEnumeration(Enum):
    I_BEACON = "iBeacon"
    EDDYSTONE = "Eddystone"
    VDV431 = "VDV431"
