from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BeaconTypeEnumeration(Enum):
    BLE = "ble"
    UWB = "uwb"
    WIFI = "wifi"
