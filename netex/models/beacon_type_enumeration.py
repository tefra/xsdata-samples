from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BeaconTypeEnumeration(StrEnum):
    BLE = "ble"
    UWB = "uwb"
    WIFI = "wifi"
