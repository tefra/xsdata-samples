from __future__ import annotations

from dataclasses import dataclass

from .type_of_retail_device_ref_structure import TypeOfRetailDeviceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfRetailDeviceRef(TypeOfRetailDeviceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
