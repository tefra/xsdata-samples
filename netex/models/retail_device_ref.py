from __future__ import annotations

from dataclasses import dataclass

from .retail_device_ref_structure import RetailDeviceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailDeviceRef(RetailDeviceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
