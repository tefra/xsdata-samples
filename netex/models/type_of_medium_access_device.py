from __future__ import annotations

from dataclasses import dataclass

from .type_of_medium_access_device_value_structure import (
    TypeOfMediumAccessDeviceValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfMediumAccessDevice(TypeOfMediumAccessDeviceValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
