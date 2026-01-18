from __future__ import annotations

from dataclasses import dataclass

from .mobile_device_ref_structure import MobileDeviceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MobileDeviceRef(MobileDeviceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
