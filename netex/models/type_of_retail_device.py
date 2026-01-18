from __future__ import annotations

from dataclasses import dataclass

from .type_of_retail_device_version_structure import (
    TypeOfRetailDeviceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfRetailDevice(TypeOfRetailDeviceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
